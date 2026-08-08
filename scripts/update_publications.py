import re
import requests

ORCID = "0000-0002-6089-032X"
HEADERS = {"Accept": "application/json"}
BIB_PATH = "_bibliography/papers_wajdi.bib"
NUM_SELECTED = 4  # how many recent papers to flag selected={true}

# Manual corrections for known-wrong author names coming from ORCID/Crossref
# (e.g. misparsed given/family names, publisher typos). Add more pairs as you spot them.
NAME_CORRECTIONS = {
    "Wajdi Ahmed": "Wajdi Alnoush",
}
 
def correct_author_name(name):
    return NAME_CORRECTIONS.get(name, name)

# Words that should stay lowercase in title case (unless they're the first word)
LOWERCASE_WORDS = {"a", "an", "the", "of", "and", "or", "for", "in", "on", "at", "to", "with", "via"}
JOURNAL_CORRECTIONS = {"methodsx": "MethodsX","acs energy letters": "ACS Energy Letters",}

def normalize_journal_name(name):
    if not name:
        return name
    
    # Check manual corrections first (case-insensitive match)
    override = JOURNAL_CORRECTIONS.get(name.strip().lower())
    if override:
        return override
    
    # Only fix names that are ALL CAPS (or close to it) -- leave normally-cased names untouched
    letters = [c for c in name if c.isalpha()]
    if not letters or not all(c.isupper() for c in letters):
        return name
    words = name.split()
    result = []
    for i, word in enumerate(words):
        lower = word.lower()
        if i > 0 and lower in LOWERCASE_WORDS:
            result.append(lower)
        else:
            result.append(lower.capitalize())
    return " ".join(result)

# -----------------------------
# Retrieve publications from ORCID
# -----------------------------
works = requests.get(f"https://pub.orcid.org/v3.0/{ORCID}/works", headers=HEADERS).json()["group"]

papers = []
for work in works:
    summary = work["work-summary"][0]
    put_code = summary["put-code"]
    paper = requests.get(f"https://pub.orcid.org/v3.0/{ORCID}/work/{put_code}", headers=HEADERS).json()

    title = paper.get("title", {}).get("title", {}).get("value", "Untitled")
    # journal = paper.get("journal-title", {}).get("value", "")
    journal = normalize_journal_name(paper.get("journal-title", {}).get("value", ""))
    year = paper.get("publication-date", {}).get("year", {}).get("value", "")

    doi = ""
    for ext in paper.get("external-ids", {}).get("external-id", []):
        if ext.get("external-id-type", "").lower() == "doi":
            doi = ext.get("external-id-value", "")
            break

    authors = []
    for contributor in paper.get("contributors", {}).get("contributor", []):
        credit_name = contributor.get("credit-name")
        if credit_name and "value" in credit_name:
            authors.append(credit_name["value"])

# Fallback: if ORCID didn't supply author names, fetch them from Crossref using the DOI
    if not authors and doi:
        try:
            cr = requests.get(f"https://api.crossref.org/works/{doi}", headers=HEADERS, timeout=10).json()
            cr_authors = cr.get("message", {}).get("author", [])
            for a in cr_authors:
                given = a.get("given", "")
                family = a.get("family", "")
                full_name = f"{given} {family}".strip()
                if full_name:
                    authors.append(full_name)
        except Exception:
            pass  # leave authors empty if Crossref lookup fails; falls back to "Unknown" downstream

    papers.append({"title": title,"journal": journal,"year": int(year) if year.isdigit() else 0,"doi": doi,"authors": authors,})

# -----------------------------
# Sort newest first
# -----------------------------
papers.sort(key=lambda p: p["year"], reverse=True)

# -----------------------------
# Helpers for BibTeX formatting
# -----------------------------
def slugify(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())

def make_cite_key(paper):
    first_author_last = paper["authors"][0].split()[-1] if paper["authors"] else "unknown"
    first_word = paper["title"].split()[0] if paper["title"] else "untitled"
    return f"{slugify(first_author_last)}{paper['year']}{slugify(first_word)}"

def escape_bibtex(text):
    return text.replace("{", "\\{").replace("}", "\\}")

def format_authors(authors):
    return " and ".join(authors) if authors else "Unknown"

# -----------------------------
# Build BibTeX entries
# -----------------------------
entries = []
for i, paper in enumerate(papers):
    key = make_cite_key(paper)
    selected = "true" if i < NUM_SELECTED else "false"

    fields = [
        f'  title = {{{escape_bibtex(paper["title"])}}}',
        f'  author = {{{escape_bibtex(format_authors(paper["authors"]))}}}',
    ]
    if paper["journal"]:
        fields.append(f'  journal = {{{escape_bibtex(paper["journal"])}}}')
    if paper["year"]:
        fields.append(f'  year = {{{paper["year"]}}}')
    if paper["doi"]:
        fields.append(f'  doi = {{{paper["doi"]}}}')
    fields.append(f"  selected = {{{selected}}}")

    entry = "@article{" + key + ",\n" + ",\n".join(fields) + "\n}\n"
    entries.append(entry)

new_block = "\n".join(entries)

# -----------------------------
# Update _bibliography/papers.bib
# -----------------------------
START = "% AUTO-PUBLICATIONS:START"
END = "% AUTO-PUBLICATIONS:END"

with open(BIB_PATH, "r", encoding="utf-8") as f:
    bib = f.read()

if START in bib and END in bib:
    before = bib.split(START)[0]
    after = bib.split(END)[1]
else:
    before = bib.rstrip() + "\n\n"
    after = ""

new_bib = before + START + "\n\n" + new_block + "\n" + END + after

with open(BIB_PATH, "w", encoding="utf-8") as f:
    f.write(new_bib)

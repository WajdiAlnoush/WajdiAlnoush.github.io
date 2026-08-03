---
layout: about
title: About
permalink: /
subtitle: ""

profile:
  align: left
  image: prof_pic.jpg
  image_circular: true # crops the image to make it circular
  more_info: false #>
    #<p>555 your office number</p> 
    #<p>123 your address street</p>
    #<p>ON, Canada</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---
<style>
  .post-header {
    display: none;
  }
</style>

Wajdi Alnoush
Postdoc <a href='#'>Affiliations</a>.<br> Address.
Previously: CC <a href='https://co2cert.com/'>@CO2CERT</a>, PhD <a href='https://www.mcmaster.ca/'>@McMasterU</a> , MSc and BSc <a href='https://www.tamu.edu/'>@TAMU</a>  Link to [subreddit](https://www.reddit.com). You can also disable any of these elements by editing `profile` property of the YAML header of your `_pages/about.md`. Edit `_bibliography/papers.bib` and Jekyll will render your [publications page](/al-folio/publications/) automatically.

T use [Font Awesome icons](https://fontawesome.com/) and [Academicons](https://jpswalsh.github.io/academicons/), like the ones below.


#div class="card mt-3"> 
#div class="card-body"> 
#h4 class="card-title">About
<div style="border: 1px solid #ffffff; border-radius: 10px; padding: 1.5rem; background-color: transparent;">
  <h4>About</h4>
    <p>
      I am a researcher working at the intersection of chemical engineering, materials science, and data science. I am passionate about teaching, scientific illustration, and dataViz.
      I co-created and maintain <a href="#">Package1</a> and <a href="#">Package2</a>, along with several other
      open-source projects. Lately I've been focusing on how XX can speed up YY.
    </p>
    <hr style="border-color: rgba(255,255,255,0.3)">
    <h4 class="card-title">Recent publications</h4>
    {% include selected_papers.liquid %}
  #/div>
</div>
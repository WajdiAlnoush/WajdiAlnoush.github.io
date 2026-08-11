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

selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page

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
  .post-header {display: none;}
  @media (min-width: 576px) {
    .profile {width: 180px !important;}}
  .profile.float-left figure {width: 160px !important; height: 160px !important; margin: 0 !important;}
  img[src*="prof_pic"] {width: 160px !important; height: 160px !important; display: block !important;}
  .bibliography .col-sm-2.abbr {display: none !important;}
  .bibliography .col-sm-8 {flex: 0 0 100% !important; max-width: 100% !important; width: 100% !important;}
  .bibliography .title,
  .bibliography .title a {
    color: var(--global-theme-color, #4fc3f7) !important;
    font-size: 1.15rem !important; font-weight: 625 !important;}


  .btn.btn-sm.z-depth-0[href*="doi.org"] {
    border: none !important; background: transparent !important; box-shadow: none !important;
    font-size: 0; /* hides the "DOI" text */
    padding: 0 !important;}

  .btn.btn-sm.z-depth-0[href*="doi.org"]::before {
    font: var(--fa-font-solid);
    content: "\f35d"; font-size: 1rem; margin-top: 7px;}
    
</style>

<!-- <span style="font-size: 2rem; font-weight: 720; display: block; margin-bottom: 0.1rem;">Wajdi Alnoush</span>

<span style="font-size: 1rem; font-weight: 470;">Postdoc <a href='#'>@Employer</a><br>
<span>

<span style="font-size: 1rem; font-weight: 470;">Previously: Visiting Research Scientist <a href='https://co2cert.com/'>@CO2CERT</a>, Research Associate <a href='https://www.tamu.edu/'>@TAMU</a> <br>
PhD <a href='https://www.mcmaster.ca/'>@McMaster</a>, MSc & BSc <a href='https://www.tamu.edu/'>@TAMU</a> </span style="color: #9ca3af;"> 
<br><br> -->

<div style="margin-left: 20px;">
  <span style="font-size: 2rem; font-weight: 720; display: block; margin-bottom: 0.08rem;">Wajdi Alnoush</span>
  <span style="font-size: 1.05rem; font-weight: 400;">
    Postdoctoral Research Fellow <a href='#'>@Employer</a><br>
    <span style="color: #7c8591;">
      Previously: Visiting Research Scientist <a href='https://co2cert.com/'>@CO2CERT</a>, Research Associate <a href='https://www.tamu.edu/'>@TAMU</a> <br>
      PhD <a href='https://www.mcmaster.ca/'>@McMaster</a>, MSc & BSc <a href='https://www.tamu.edu/'>@TAMU</a>
    </span>
  </span>
</div>

<div style="margin-top: 0.45rem; margin-bottom: 1rem;">
  <a href="mailto:your.email@example.com" style="margin-right: 4.75px; font-size: 1.7rem;"><i class="fas fa-envelope"></i></a>
  <a href="https://github.com/WajdiAlnoush" style="margin-right: 4.75px; font-size: 1.7rem;"><i class="fab fa-github"></i></a>
  <a href="https://www.linkedin.com/in/wajdi-alnoush/" style="margin-right: 4.75px; font-size: 1.7rem;"><i class="fab fa-linkedin"></i></a>
  <a href="/feed.xml" style="margin-right: 4.75px; font-size: 1.7rem;"><i class="fas fa-rss"></i></a>
  <a href="https://scholar.google.com/citations?user=your-id" style="margin-right: 5px; font-size: 1.7rem;"><i class="ai ai-google-scholar"></i></a>

  <a href="{{ '/assets/pdf/Wajdi_Alnoush_CV.pdf' | relative_url }}" style="margin-right: 4.75px; display: inline-block; vertical-align: middle;" aria-label="Curriculum Vitae" title="Curriculum Vitae"> <img src="{{ '/assets/img/cv-icon.png' | relative_url }}" alt="CV" style="width: 26px; height: 23.9px; object-fit: contain; vertical-align: middle;position: relative; top: -5.2px;"></a>
</div>

<div style="border: 0.4px solid #6b7280; border-radius: 10px; padding: 1.5rem; background-color: transparent; clear: both;">
  <h4 style="font-size: 1.5rem; font-weight: 700;">About</h4>
    <p style="font-size: 1.05rem; font-weight: 390;">
      I am a researcher working at the intersection of chemical engineering, materials science, and data science. I am passionate about teaching, scientific illustration, and dataViz.
      I co-created and maintain <a href="#">Package1</a> and <a href="#">Package2</a>, along with several other
      open-source projects. Lately I've been focusing on how XX can speed up YY.
    </p>
    <hr style="border: none; border-top: 0.4px solid #6b7280; margin: 1rem 0;">
    <h4 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.8rem;" class="card-title"><br>Recent publications</h4>
    {% include selected_papers.liquid %}
    
</div>
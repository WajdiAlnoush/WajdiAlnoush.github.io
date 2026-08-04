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
    display: none;}
  img[src*="prof_pic"] {
    width: 170px !important;
    height: 170px !important;  
</style>

<span style="font-size: 2rem; font-weight: 720; display: block; margin-bottom: 0.1rem;">Wajdi Alnoush</span>
<span style="font-size: 1.15rem; font-weight: 490;">Postdoc <a href='#'>@Employer</a><br>
Previously: Visiting Research Scientist <a href='https://co2cert.com/'>@CO2CERT</a>, Research Associate <a href='https://www.tamu.edu/'>@TAMU</a> <br>
PhD <a href='https://www.mcmaster.ca/'>@McMaster</a>, MSc & BSc <a href='https://www.tamu.edu/'>@TAMU</a> </span> 
<br><br>


<br>
<div style="border: 0.4px solid #6b7280; border-radius: 10px; padding: 1.5rem; background-color: transparent;">
  <h4 style="font-size: 1.5rem; font-weight: 700;">About</h4>
    <p style="font-size: 1.05rem; font-weight: 490;">
      I am a researcher working at the intersection of chemical engineering, materials science, and data science. I am passionate about teaching, scientific illustration, and dataViz.
      I co-created and maintain <a href="#">Package1</a> and <a href="#">Package2</a>, along with several other
      open-source projects. Lately I've been focusing on how XX can speed up YY.
    </p>
    <hr style="border-color: rgba(255,255,255,0.3)">
    <h4 style="font-size: 1.5rem; font-weight: 700;" class="card-title"><br>Recent publications</h4>
    {% include selected_papers.liquid %}
</div>
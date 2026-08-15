---
layout: page
permalink: /publications/
title: Publications
description: Peer-reviewed publications categorized in reversed chronological order. 
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->
<!-- Bibsearch Feature -->

<style>
  .bibliography .col-sm-2.abbr {display: none !important;}
  .bibliography .col-sm-8 {flex: 0 0 100% !important; max-width: 100% !important; width: 100% !important;}
  .bibliography .title,
  .bibliography .title a {color: var(--global-theme-color, #4fc3f7) !important; font-size: 1.15rem !important; font-weight: 625 !important;} 
  h2.bibliography {font-size: 1.4rem !important; font-weight: 600 !important;}

  .publications {border: 0.4px solid #6b7280; border-radius: 10px; padding: 1.5rem; background-color: transparent;}

  /* .btn.btn-sm.z-depth-0[href*="doi.org"] {font-size: 0;} */
  /* .btn.btn-sm.z-depth-0[href*="doi.org"]::before {
    content: "🔗";} */

  .btn.btn-sm.z-depth-0[href*="doi.org"] {
    border: none !important; background: transparent !important; box-shadow: none !important;
    font-size: 0; /* hides the "DOI" text */
    padding: 0 !important;}

  .btn.btn-sm.z-depth-0[href*="doi.org"]::before {font: var(--fa-font-solid); content: "\f35d"; font-size: 1rem; margin-top: 7px;}
</style>

<div class="publications">
    {% bibliography %}
</div>

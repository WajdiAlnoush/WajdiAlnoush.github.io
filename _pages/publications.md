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
  .bibliography .col-sm-8 {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    width: 100% !important;}

  .bibliography .title,
  .bibliography .title a {color: var(--global-theme-color, #4fc3f7) !important; font-size: 1.1rem !important;
    font-weight: 600 !important;} 

  .publications {
    border: 0.4px solid #6b7280;
    border-radius: 10px;
    padding: 1.5rem;
    background-color: transparent;}
</style>


<div class="publications">
    {% bibliography %}
</div>

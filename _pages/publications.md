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
  .bibliography .col-sm-2.abbr {
    display: none !important;
  }
  .bibliography .col-sm-8 {
    flex: 0 0 100% !important;
    max-width: 100% !important;
    width: 100% !important;
  }

  /* 1. Title links match the site's link blue */
  .bibliography .title,
  .bibliography .title a {
    color: var(--global-theme-color, #4fc3f7) !important;
  }

  /* 2. Frame around the whole publications block */
  .publications {
    border: 0.4px solid #6b7280;
    border-radius: 10px;
    padding: 1.5rem;
    background-color: transparent;
  }

  /* 3. Bolder year headers */
  .publications h2.bibliography {
    font-weight: 800 !important;
  }
</style>



<div class="publications">
  {% bibliography %}
</div>

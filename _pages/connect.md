---
layout: page
permalink: /connect/
title: Connect
description: If you'd like to connect, you can book a meeting with me using the calendar below.
nav: true
nav_order: 6
calendar: true
---

<!-- {% include calendar.liquid calendar_id='wajdi.alnoush@gmail.com' timezone='America/Toronto' %} -->

<div style="margin-top: 1.5rem;">
  <link href="https://calendar.google.com/calendar/scheduling-button-script.css" rel="stylesheet">
  <script src="https://calendar.google.com/calendar/scheduling-button-script.js" async></script>

  <script>
    window.addEventListener('load', function () {
      calendar.schedulingButton.load({url: 'https://calendar.app.google/NcTKFsykfF5UKwQe9?gv=true',
        color: '#4fc3f7', label: 'Book a meeting', target: document.getElementById('booking-button')});
    });
  </script>

  <button id="booking-button" class="btn btn-primary">
    <i class="fa-regular fa-calendar"></i>
    Book a meeting
  </button>
</div>
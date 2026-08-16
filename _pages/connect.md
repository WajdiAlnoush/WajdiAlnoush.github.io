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

<!-- <style>
  .connect-btn {font-size: 0.85rem; margin-right: 10px; margin-bottom: 10px;}
  .anon-form {max-width: 500px; margin-top: 1.5rem;}
  .anon-form textarea {width: 100%; min-height: 100px; padding: 0.6rem; border-radius: 8px;     border: 0.4px solid #6b7280; background: transparent; color: inherit;font-family: inherit; resize: vertical;}
  .anon-form button {margin-top: 0.6rem;}
</style>

<div style="margin-top: 1.5rem;">
  <link href="https://calendar.google.com/calendar/scheduling-button-script.css" rel="stylesheet">
  <script src="https://calendar.google.com/calendar/scheduling-button-script.js" async></script>

  <script>
    window.addEventListener('load', function () {
      calendar.schedulingButton.load({url: 'https://calendar.app.google/NcTKFsykfF5UKwQe9?gv=true',
        color: '#4fc3f7', label: 'Book a meeting', target: document.getElementById('booking-button')});});
  </script>

  <button id="booking-button" class="btn btn-primary" style="font-size: 0.85rem;">
    <i class="fa-regular fa-calendar"></i>
    Book a meeting
  </button>
</div>

<div class="anon-form">
  <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Send me an anonymous message</h4>
  <form action="https://formspree.io/f/xqpzdkkp" method="POST">
    <textarea name="message" placeholder="Type your message here..." required></textarea>
    <br>
    <button type="submit" class="btn btn-primary connect-btn">
      <i class="fa-regular fa-comment-dots"></i>
      Send anonymously
    </button>
  </form>
</div>

<div style="margin-top: 2rem;">
  <h4 style="font-size: 1.2rem; font-weight: 700; margin-bottom: 0.5rem;">Support my work</h4>
  <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="wajdialnoush" data-color="#FFDD00" data-emoji="☕" data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff"></script>
</div> -->

<style>
  .connect-row {display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; padding: 1.25rem 0; border-bottom: 0.4px solid #6b7280;}
  .connect-row:last-child {border-bottom: none;}
  .connect-label {font-size: 1rem; font-weight: 600; display: flex; align-items: center; gap: 0.4rem; flex-shrink: 0;}
  .connect-control {flex: 1 1 auto; max-width: 440px; display: flex; justify-content: flex-end;}
  /* #booking-button button {font-size: 0.95rem !important; font-weight: 600; display: inline-flex !important; align-items: center !important; justify-content: center !important;} */

  /* Anonymous message: textarea + button combined into one control */
  .anon-wrapper {display: flex; align-items: center; gap: 0.8rem; width: 100%;}
  .anon-wrapper textarea {flex: 1 1 auto; padding: 0.5rem 0.65rem; border-radius: 8px; border: 0.4px solid #6b7280;
    background: transparent; color: inherit; font-family: inherit; font-size: 0.9rem; font-weight: 450; resize: none; overflow: hidden; min-height: 40px; line-height: 1.1; align-content: center;}
  .anon-wrapper button {flex-shrink: 0; font-size: 1rem; font-weight: 600; margin-left: auto; white-space: nowrap; background-color: var(--global-theme-color, #4fc3f7); color: #ffffff; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border:none; border-radius: 8px; padding: 6px 12px; cursor:pointer; width: 175px; height: 40px;}
  /* The book a meeting button */
  .qxCTlb {width: 175px !important; height: 40px !important; font-size: 0.95rem !important; font-weight: 450; border-radius: 8px !important; color: #ffffff !important; margin-right: 6px;}
  /* The buy me a coffee button */
  .bmc-btn {transform: scale(0.767) !important; transform-origin: right center !important; margin-right: 7px;}
</style>

<div class="connect-row">
  <!-- <div class="connect-label"><i class="fa-regular fa-calendar"></i> Book a meeting</div> -->
  <div class="connect-label"><i class="fa-brands fa-google"></i> Book a meeting</div>
  <div class="connect-control">
    <link href="https://calendar.google.com/calendar/scheduling-button-script.css" rel="stylesheet">
    <script src="https://calendar.google.com/calendar/scheduling-button-script.js" async></script>
    <script>
      window.addEventListener('load', function () {calendar.schedulingButton.load({
          url: 'https://calendar.app.google/NcTKFsykfF5UKwQe9?gv=true', color: '#7fb8a3', label: 'Book a meeting',
          target: document.getElementById('booking-button')});
      });
    </script>
    <div id="booking-button"></div>
  </div>
</div>

<div class="connect-row">
  <div class="connect-label"><i class="fa-regular fa-comment-dots"></i> Send me an anonymous message</div>
  <div class="connect-control">
    <form action="https://formspree.io/f/xqpzdkkp" method="POST" class="anon-wrapper">
      <textarea name="message" id="anon-textarea" placeholder="Type your message here..." rows="1" required></textarea>
      <button type="submit" class="btn btn-primary">Send anonymously</button>
    </form>
  </div>
</div>

<div class="connect-row">
  <div class="connect-label">☕ Support my work</div>
  <div class="connect-control">
    <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="wajdialnoush" data-color="#FFD966" data-emoji="☕" data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#000000"></script>
  </div>
</div>

<script>
  // Auto-grow the anonymous message textarea as the user types
  const anonTextarea = document.getElementById('anon-textarea');
  anonTextarea.addEventListener('input', function () {this.style.height = 'auto'; this.style.height = this.scrollHeight + 'px';});
</script>
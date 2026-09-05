---
layout: page
permalink: /ProgressTrack/
title: 
nav: false
---

<style>
  .password-gate {text-align: center; padding: 4rem 1rem; max-width: 400px; margin: 0 auto;}
  .password-gate input {padding: 0.6rem 0.8rem; border-radius: 8px; border: 0.4px solid #6b7280; background: transparent; color: inherit; font-family: inherit; font-size: 0.95rem; margin-right: 0.5rem; margin-top: 1rem;}
  .password-gate button {padding: 0.6rem 1.2rem; border-radius: 8px; border: none; background-color: var(--global-theme-color, #4fc3f7); color: #000; font-weight: 700; cursor: pointer;}
  .password-gate p.error {color: #e76f51; font-size: 0.85rem; margin-top: 0.6rem; display: none;}

  /* Project Card Styles */  
  .project-card {background:rgba(255, 255, 255, 0.02); border-radius: 16px; padding: 1.1rem 1.25rem 1.1rem 1.5rem; margin-bottom: 1.25rem; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.07); border: 0.5px solid var(--global-border-color, #e8e8e8); transition: transform 0.2s ease, box-shadow 0.2s ease;}

  .project-card:hover {transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);}
  .project-header {display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 0.2rem;}
  .project-title {font-size: 1.5rem; font-weight: 700; margin-bottom: 0.2rem; margin: 0; color: var(--global-text-color, #2c3e50);}
  .project-hours {font-size: 0.95rem; color: var(--global-text-color-secondary, #6b7280);font-weight: 500;}
  /* .project-hours span {font-weight: 700; color: var(--global-theme-color, #4fc3f7);} */
  .project-hours span {font-weight: 700;}
  .project-hours span.color-filled { color: #4fc3f7; }
  .project-hours span.color-filled-green { color: #2ecc71; }
  .project-hours span.color-filled-purple { color: #9b59b6; }
  .project-hours span.color-filled-orange { color: #e67e22; }
  .project-hours span.color-filled-pink { color: #e74c3c; }
  
  .project-description {margin: 0.2rem 0 0.75rem 0; color: var(--global-text-color-secondary, #6b7280); font-size: 0.95rem;}

  /* Mini-box grid */
  .hour-grid {display: grid; grid-template-columns: repeat(36, 18px); gap: 3.75px; margin-top: 0.75rem;}
  .hour-box {width:18px; height:18px; border-radius: 4px; background: var(--global-border-color, #2c3e50);
    transition: background 0.15s ease, transform 0.15s ease; cursor: default;flex-shrink: 0; }
  
  /* For smaller screens - keep boxes fixed but reduce grid columns */
  @media (max-width: 768px) {
  .hour-grid {grid-template-columns: repeat(15, 18px); gap: 3px;}
  .hour-box {width: 18px; height: 18px;}}

  @media (max-width: 480px) {
  .hour-grid {grid-template-columns: repeat(10, 16px); gap: 3px;}
  .hour-box {width: 16px; height: 16px;}}

  .hour-box.filled {background:  #4fc3f7;}
  .hour-box.filled-dark {background: #2c3e50;}
  .hour-box.filled-green {background: #2ecc71;}
  .hour-box.filled-purple {background: #9b59b6;}
  .hour-box.filled-orange {background: #e67e22;}
  .hour-box.filled-pink {background: #e74c3c;}
  .hour-box:hover {transform: scale(1.12); z-index: 2;}

  .hour-grid-label {display: flex; justify-content: space-between; font-size: 0.7rem; color: var(--global-text-color-secondary, #6b7280); margin-top: 0.3rem; padding: 0 2px;}
  .project-footer {margin-top: 0.75rem; display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: var(--global-text-color-secondary, #6b7280);}
  .progress-percentage {font-weight: 600; color: var(--global-theme-color, #4fc3f7);}

  /* Responsive */
  @media (max-width: 768px) {
    .project-card {padding: 1rem 1rem 1.5rem 1rem;}
    .project-title {font-size: 1.2rem;}
    .hour-grid {grid-template-columns: repeat(15, 1fr); gap: 3px;}
    .hour-box {min-width: 10px; min-height: 10px;}}

  @media (max-width: 480px) {
    .hour-grid {grid-template-columns: repeat(10, 1fr); gap: 3px;}
    .project-header {flex-direction: column; align-items: flex-start; gap: 0.25rem;}}
</style>

<div id="password-gate" class="password-gate">
  <p>Enter password to view 👀</p>
  <div>
    <input type="password" id="page-password" placeholder="Enter password">
    <button onclick="checkPassword()">Unlock</button>
  </div>
  <p class="error" id="wrong-password-msg">Wrong password, try again!</p>
</div>

<div id="protected-content" style="display: none;">
  
  <div class="post">
    <h1> Progress Tracking</h1>
    <p style="color: var(--global-text-color-secondary, #6b7280); margin-bottom: 2rem;">
      Each mini-box represents 20 minutes of focused work.
    </p>

    <!-- PROJECT 1 -->
    <div class="project-card">
      <div class="project-header">
        <h2 class="project-title">Rejected paper</h2>
        <div class="project-hours">
          <span id="hours-done-1" class="color-filled">12</span> / <span id="hours-total-1" class="color-filled">40</span> hrs
        </div>
      </div>
      <p class="project-description">Designing and coding a personal portfolio site.</p>
      
      <div class="hour-grid" id="grid-1">
        <!-- Will be populated by JavaScript -->
      </div>
      
      <div class="project-footer">
        <span>🎯 <span id="progress-pct-1">30</span>% complete</span>
        <span>⏱️ <span id="hours-remaining-1">28</span> hrs to go</span>
      </div>
    </div>

    <!-- PROJECT 2 -->
    <div class="project-card">
      <div class="project-header">
        <h2 class="project-title">Pore-Network Paper</h2>
        <div class="project-hours">
          <span id="hours-done-2" class="color-filled-green">8</span> / <span id="hours-total-2" class="color-filled-green">50</span> hrs
        </div>
      </div>
      <p class="project-description">Mastering Python for data science and automation.</p>
      
      <div class="hour-grid" id="grid-2">
        <!-- Will be populated by JavaScript -->
      </div>
      
      <div class="project-footer">
        <span>🎯 <span id="progress-pct-2">16</span>% complete</span>
        <span>⏱️ <span id="hours-remaining-2">42</span> hrs to go</span>
      </div>
    </div>

    <!-- PROJECT 3 -->
    <div class="project-card">
      <div class="project-header">
        <h2 class="project-title">Fundamentals of Reservoir Fluids</h2>
        <div class="project-hours">
          <span id="hours-done-3" class="color-filled-purple">15</span> / <span id="hours-total-3" class="color-filled-purple">100</span> hrs
        </div>
      </div>
      <p class="project-description">Consistent workout routine and health tracking.</p>
      
      <div class="hour-grid" id="grid-3">
        <!-- Will be populated by JavaScript -->
      </div>
      
      <div class="project-footer">
        <span>🎯 <span id="progress-pct-3">15</span>% complete</span>
        <span>⏱️ <span id="hours-remaining-3">85</span> hrs to go</span>
      </div>
    </div>

    <!-- PROJECT 4 -->
    <div class="project-card">
      <div class="project-header">
        <h2 class="project-title">XAS Reactor Paper</h2>
        <div class="project-hours">
          <span id="hours-done-4" class="color-filled-orange">6</span> / <span id="hours-total-4" class="color-filled-orange">30</span> hrs
        </div>
      </div>
      <p class="project-description">Reading 12 books this year.</p>
      
      <div class="hour-grid" id="grid-4">
        <!-- Will be populated by JavaScript -->
      </div>
      
      <div class="project-footer">
        <span>🎯 <span id="progress-pct-4">20</span>% complete</span>
        <span>⏱️ <span id="hours-remaining-4">24</span> hrs to go</span>
      </div>
    </div>

    <!-- PROJECT 5 -->
    <div class="project-card">
      <div class="project-header">
        <h2 class="project-title">Reverse Sweep Paper</h2>
        <div class="project-hours">
          <span id="hours-done-5" class="color-filled-pink">6</span> / <span id="hours-total-5" class="color-filled-pink">30</span> hrs
        </div>
      </div>
      <p class="project-description">Reading 12 books this year.</p>
      
      <div class="hour-grid" id="grid-5">
        <!-- Will be populated by JavaScript -->
      </div>
      
      <div class="project-footer">
        <span>🎯 <span id="progress-pct-5">20</span>% complete</span>
        <span>⏱️ <span id="hours-remaining-5">24</span> hrs to go</span>
      </div>
    </div>

    <!-- PROJECT 6 -->
    <div class="project-card">
      <div class="project-header">
        <h2 class="project-title">Reverse Sweep Paper</h2>
        <div class="project-hours">
          <span id="hours-done-6" class="color-filled-green">6</span> / <span id="hours-total-6" class="color-filled-green">30</span> hrs
        </div>
      </div>
      <p class="project-description">Reading 12 books this year.</p>
      
      <div class="hour-grid" id="grid-6">
        <!-- Will be populated by JavaScript -->
      </div>
      
      <div class="project-footer">
        <span>🎯 <span id="progress-pct-6">20</span>% complete</span>
        <span>⏱️ <span id="hours-remaining-6">24</span> hrs to go</span>
      </div>
    </div>

    <div style="text-align: center; margin-top: 2rem; margin-bottom: 2rem; padding: 0.75rem; background: var(--global-card-bg-color, #f8f9fa); border-radius: 12px;">
      <p style="font-size: 0.9rem; color: var(--global-text-color-secondary, #6b7280);">
        💡 Click on any mini-box to mark the completion of a 20-min focus session!
      </p>
    </div>
  </div>

</div>

<script>
  const SESSION_MINUTES = 20;
  const SESSIONS_PER_HOUR = 60 / SESSION_MINUTES; // = 3

  // Project data is stored in SESSIONS internally (each box = 1 session = 20 min)
  // doneHours/totalHours below are just the *initial* values you set, converted once at load
  const projects = [
    { id: 1, doneHours: 12, totalHours: 40, color: 'filled' },
    { id: 2, doneHours: 8,  totalHours: 50, color: 'filled-green' },
    { id: 3, doneHours: 15, totalHours: 100, color: 'filled-purple' },
    { id: 4, doneHours: 6,  totalHours: 30, color: 'filled-orange' },
    { id: 5, doneHours: 6,  totalHours: 28, color: 'filled-pink' },
    { id: 6, doneHours: 10, totalHours: 34, color: 'filled-green' }
  ].map(p => ({
    id: p.id,
    color: p.color,
    doneSessions: Math.round(p.doneHours * SESSIONS_PER_HOUR),
    totalSessions: Math.round(p.totalHours * SESSIONS_PER_HOUR)
  }));

  // Raise this if you want more boxes visible before truncating with "…"
  // (totals are now 3x larger than before, since each box is 20 min instead of 1 hr)
  const MAX_BOXES = 150;

  function renderGrid(projectId, doneSessions, totalSessions, colorClass) {
    const grid = document.getElementById(`grid-${projectId}`);
    if (!grid) return;

    const displayTotal = Math.min(totalSessions, MAX_BOXES);
    const displayDone = Math.min(doneSessions, displayTotal);

    grid.innerHTML = '';

    for (let i = 0; i < displayDone; i++) {
      const box = document.createElement('div');
      box.className = `hour-box ${colorClass}`;
      box.title = `Session ${i + 1} (20 min) completed`;
      box.addEventListener('click', function () {
        if (this.classList.contains(colorClass)) {
          this.classList.remove(colorClass);
          this.classList.add('hour-box');
          updateCounts(projectId, -1);
        } else {
          this.classList.remove('hour-box');
          this.classList.add(colorClass);
          updateCounts(projectId, 1);
        }
      });
      grid.appendChild(box);
    }

    for (let i = displayDone; i < displayTotal; i++) {
      const box = document.createElement('div');
      box.className = 'hour-box';
      box.title = `Session ${i + 1} (20 min) - not yet completed`;
      box.addEventListener('click', function () {
        if (!this.classList.contains(colorClass)) {
          this.classList.remove('hour-box');
          this.classList.add(colorClass);
          updateCounts(projectId, 1);
        }
      });
      grid.appendChild(box);
    }

    if (totalSessions > MAX_BOXES) {
      const ellipsis = document.createElement('div');
      ellipsis.style.cssText = `
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        color: var(--global-text-color-secondary, #6b7280);
        aspect-ratio: 1;
        min-width: 12px;
        min-height: 12px;
      `;
      ellipsis.textContent = '…';
      ellipsis.title = `${totalSessions - MAX_BOXES} more sessions not shown`;
      grid.appendChild(ellipsis);
    }
  }

  function formatHours(sessions) {
    // Convert sessions back to hours, trimming to at most 1 decimal place
    const hrs = sessions / SESSIONS_PER_HOUR;
    return Number.isInteger(hrs) ? hrs : hrs.toFixed(1);
  }

  function updateCounts(projectId, deltaSessions) {
    const project = projects.find(p => p.id === projectId);
    if (!project) return;

    const newDoneSessions = Math.max(0, Math.min(project.doneSessions + deltaSessions, project.totalSessions));
    project.doneSessions = newDoneSessions;

    const doneHours = formatHours(newDoneSessions);
    const totalHours = formatHours(project.totalSessions);
    const remainingHours = formatHours(project.totalSessions - newDoneSessions);

    document.getElementById(`hours-done-${projectId}`).textContent = doneHours;
    document.getElementById(`hours-total-${projectId}`).textContent = totalHours;
    document.getElementById(`hours-remaining-${projectId}`).textContent = remainingHours;

    const pct = Math.round((newDoneSessions / project.totalSessions) * 100);
    document.getElementById(`progress-pct-${projectId}`).textContent = pct;

    renderGrid(projectId, newDoneSessions, project.totalSessions, project.color);
  }

  function checkPassword() {
    const input = document.getElementById('page-password').value;
    const errorMsg = document.getElementById('wrong-password-msg');
    if (input === "Nayef2026" || input === "Wajdi2026") {
      document.getElementById('password-gate').style.display = 'none';
      document.getElementById('protected-content').style.display = 'block';
      sessionStorage.setItem('progressUnlocked', 'true');
      initializeGrids();
    } else {
      errorMsg.style.display = 'block';
    }
  }

  function initializeGrids() {
    projects.forEach(p => {
      // Also sync the initial displayed hours/percent labels on first load,
      // in case they don't already match your HTML's hardcoded starting numbers
      document.getElementById(`hours-done-${p.id}`).textContent = formatHours(p.doneSessions);
      document.getElementById(`hours-total-${p.id}`).textContent = formatHours(p.totalSessions);
      document.getElementById(`hours-remaining-${p.id}`).textContent = formatHours(p.totalSessions - p.doneSessions);
      const pct = Math.round((p.doneSessions / p.totalSessions) * 100);
      document.getElementById(`progress-pct-${p.id}`).textContent = pct;

      renderGrid(p.id, p.doneSessions, p.totalSessions, p.color);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    if (sessionStorage.getItem('progressUnlocked') === 'true') {
      document.getElementById('password-gate').style.display = 'none';
      document.getElementById('protected-content').style.display = 'block';
      initializeGrids();
    }
  });

  document.getElementById('page-password').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      checkPassword();
    }
  });
</script>


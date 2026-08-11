---
layout: page
permalink: /whatibuild/
title: Value propisition. 
description: What I design, build, and bring value to.
nav: true
nav_order: 4
calendar: true
---
<style>
  .build-section {margin-top: 2.5rem;}
  .build-heading {font-size: 1.4rem; font-weight: 700; margin-bottom: 1rem; border-bottom: 1px solid #6b7280; padding-bottom: 0.5rem;}
  .build-row {display: flex; flex-wrap: wrap; gap: 1rem;}
  .build-card {border: 0.4px solid #6b7280; border-radius: 10px; padding: 1rem;
    flex: 1 1 calc(50% - 0.5rem); min-width: 280px; box-sizing: border-box;}
  .build-card-icon {display: block; width: 275px; height: 240px; object-fit: contain; margin: -18px auto -2px;}
  .build-card-title {font-size: 1.15rem; font-weight: 700; color: var(--global-theme-color, #4fc3f7); margin-bottom: -2rem;}
  .build-card-desc {color: #9ca3af; font-size: 1.05rem; margin-bottom: 0.65rem;}
  .build-card ul {margin: 0; padding-left: 1.1rem; font-size: 0.92rem;}
  .build-card ul li {margin-bottom: 0.1rem;}
  .build-card-desc-underlined {border-bottom: 1px solid #6b7280; padding-bottom: 8px;}
</style>

<div class="build-section">
  <div class="build-heading">What I Build</div>
  <div class="build-row">

    <div class="build-card">
      <div class="build-card-title">Novel Functional Materials</div>
      <!-- <svg class="build-card-icon" viewBox="0 0 48 48" fill="none" stroke="#4fc3f7" stroke-width="1.5">
        <circle cx="24" cy="8" r="3"/>
        <circle cx="10" cy="20" r="3"/>
        <circle cx="38" cy="20" r="3"/>
        <circle cx="10" cy="36" r="3"/>
        <circle cx="38" cy="36" r="3"/>
        <line x1="24" y1="11" x2="10" y2="17"/>
        <line x1="24" y1="11" x2="38" y2="17"/>
        <line x1="10" y1="23" x2="10" y2="33"/>
        <line x1="38" y1="23" x2="38" y2="33"/>
        <line x1="10" y1="20" x2="38" y2="20"/>
        <line x1="10" y1="36" x2="38" y2="36"/>
      </svg> -->

      <img class="build-card-icon" src="{{ '/assets/img/WIB_1.png' | relative_url }}" alt="Advanced characterization tools">
      <div class="build-card-desc build-card-desc-underlined">Designing and developing novel catalyic materials for sustainable energy conversion.</div>
      <ul>
        <li>PGM-free catalysts</li>
        <li>Zeolitic imidazolate framework precursors</li>
        <li>Pyrolysis and structural tuning</li>
        <li>Atomically dispersed M-N-C catalysts</li>
      </ul>
    </div>

    <div class="build-card">
      <div class="build-card-title">Advanced Characterizatoin Tools</div>
      <!-- <svg class="build-card-icon" viewBox="0 0 48 48" fill="none" stroke="#4fc3f7" stroke-width="1.5">
        <rect x="14" y="10" width="20" height="28" rx="2"/>
        <line x1="14" y1="18" x2="34" y2="18"/>
        <line x1="20" y1="6" x2="20" y2="10"/>
        <line x1="28" y1="6" x2="28" y2="10"/>
        <path d="M18 24 Q24 20 30 24 Q24 28 18 24 Z"/>
      </svg> -->

      <img class="build-card-icon" src="{{ '/assets/img/WIB_2.png' | relative_url }}" alt="Advanced characterization tools">
      <div class="build-card-desc build-card-desc-underlined">Building custom platforms to observe materials under working conditions.</div>
      <ul>
        <li>Custom electrochemical cell design</li>
        <li>Beamline-compatible geometries</li>
        <li>Real-time structural monitoring</li>
        <li>XX</li>
      </ul>
    </div>

    <div class="build-card">
      <div class="build-card-title">Experiments</div>
      <!-- <svg class="build-card-icon" viewBox="0 0 48 48" fill="none" stroke="#4fc3f7" stroke-width="1.5">
        <path d="M6 34 L14 20 L20 28 L28 12 L36 26 L42 18"/>
        <circle cx="14" cy="20" r="1.5" fill="#4fc3f7"/>
        <circle cx="28" cy="12" r="1.5" fill="#4fc3f7"/>
        <circle cx="36" cy="26" r="1.5" fill="#4fc3f7"/>
      </svg> -->

      <img class="build-card-icon" src="{{ '/assets/img/WIB_3.png' | relative_url }}" alt="Advanced characterization tools">
      <div class="build-card-desc build-card-desc-underlined">Electrochemical and spectroscopic platforms for understanding catalyst behavior.</div>
      <ul>
        <li>Rotating disk electrode (RDE) studies</li>
        <li>Impedance spectroscopy</li>
        <li>Operando XAS measurements</li>
        <li>XX</li>
      </ul>
    </div>

    <div class="build-card">
      <div class="build-card-title">Acceleration & Automation Pipelines</div>
      <!-- <svg class="build-card-icon" viewBox="0 0 48 48" fill="none" stroke="#4fc3f7" stroke-width="1.5">
        <rect x="6" y="8" width="10" height="8" rx="1"/>
        <rect x="20" y="8" width="10" height="8" rx="1"/>
        <rect x="34" y="8" width="8" height="8" rx="1"/>
        <rect x="14" y="28" width="10" height="8" rx="1"/>
        <line x1="16" y1="12" x2="20" y2="12"/>
        <line x1="30" y1="12" x2="34" y2="12"/>
        <line x1="11" y1="16" x2="11" y2="24" />
        <line x1="11" y1="24" x2="19" y2="28"/>
        <line x1="25" y1="16" x2="19" y2="28"/>
      </svg> -->
      
      <img class="build-card-icon" src="{{ '/assets/img/WIB_5.png' | relative_url }}" alt="Advanced characterization tools">
      <div class="build-card-desc build-card-desc-underlined">Python-based workflows for processing electrochemical and XAS data.</div>
      <ul>
        <li>Automated data cleaning</li>
        <li>EXAFS/XANES fitting</li>
        <li>High-throughput experiments</li>  
        <li>Reproducible batch processing</li>
      </ul>
    </div>

  </div>
</div>


<div class="build-section">
  <div class="build-heading">Growing Interests</div>
  <div class="build-row">

    <div class="build-card">
      <div class="build-card-title">Al/ML-driven Material Discovery</div>

      <!-- <svg class="build-card-icon" viewBox="0 0 48 48" fill="none" stroke="#4fc3f7" stroke-width="1.5">
        <rect x="6" y="8" width="10" height="8" rx="1"/>
        <rect x="20" y="8" width="10" height="8" rx="1"/>
        <rect x="34" y="8" width="8" height="8" rx="1"/>
        <rect x="14" y="28" width="10" height="8" rx="1"/>
        <line x1="16" y1="12" x2="20" y2="12"/>
        <line x1="30" y1="12" x2="34" y2="12"/>
        <line x1="11" y1="16" x2="11" y2="24"/>
        <line x1="11" y1="24" x2="19" y2="28"/>
        <line x1="25" y1="16" x2="19" y2="28"/>
      </svg> -->

      <img class="build-card-icon" src="{{ '/assets/img/WIB_6.png' | relative_url }}" alt="Advanced characterization tools">
      <div class="build-card-desc build-card-desc-underlined">Python-based workflows for processing electrochemical and XAS data.</div>
      <ul>
        <li>111</li>
        <li>222</li>
        <li>333</li>  
        <li>444</li>
      </ul>
    </div>

    <div class="build-card">
      <div class="build-card-title">Autonomous & Self-driving Labs</div>

      <!-- <svg class="build-card-icon" viewBox="0 0 48 48" fill="none" stroke="#4fc3f7" stroke-width="1.5">
        <rect x="6" y="8" width="10" height="8" rx="1"/>
        <rect x="20" y="8" width="10" height="8" rx="1"/>
        <rect x="34" y="8" width="8" height="8" rx="1"/>
        <rect x="14" y="28" width="10" height="8" rx="1"/>
        <line x1="16" y1="12" x2="20" y2="12"/>
        <line x1="30" y1="12" x2="34" y2="12"/>
        <line x1="11" y1="16" x2="11" y2="24" />
        <line x1="11" y1="24" x2="19" y2="28"/>
        <line x1="25" y1="16" x2="19" y2="28"/>
      </svg> -->
      <img class="build-card-icon" src="{{ '/assets/img/WIB_4.png' | relative_url }}" alt="Advanced characterization tools">
      <div class="build-card-desc build-card-desc-underlined">Python-based workflows for processing electrochemical and XAS data.</div>
      <ul>
        <li>111</li>
        <li>222</li>
        <li>333</li>  
        <li>444</li>
      </ul>
    </div>

  </div>
</div>
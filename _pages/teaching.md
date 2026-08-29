---
layout: page
permalink: /teaching/
title: Teaching
description: My teaching experience (Courses taught, certificates obtained, and development programs completed), organized by institution.
nav: true
nav_order: 4
calendar: true
---

<!-- This page displays a collection of courses with detailed schedules, materials, and resources. You can organize your courses by years, terms, or topics. -->

<!-- {% include calendar.liquid calendar_id='wajdi.alnoush@gmail.com' timezone='America/Toronto' %} -->

<style>
  .teaching-group {margin-bottom: 2.5rem;}
  .teaching-university {font-size: 1.4rem; font-weight: 700; margin-bottom: 1rem; border-bottom: 1px solid #6b7280;padding-bottom: 0.5rem;}
  .teaching-course-row {display: flex; flex-wrap: wrap; gap: 1rem;}
  .teaching-course {border: 0.4px solid #6b7280; border-radius: 10px; padding: 1.25rem; flex: 1 1 calc(50% - 0.5rem);
    min-width: 280px; box-sizing: border-box;}
  .teaching-course-title {font-size: 1.15rem; font-weight: 700; color: var(--global-theme-color, #4fc3f7);}
  .teaching-course-meta {color: #9ca3af; font-size: 0.95rem;}

  .teaching-course-desc-wrapper {position: relative; margin-top: 0.5rem;}
  .teaching-course-desc {display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; margin: 0;}
  .teaching-course-desc.expanded {display: block; -webkit-line-clamp: unset; overflow: visible;}

  .teaching-readmore {
    position: absolute;
    right: 0;
    bottom: 0;
    padding-left: 0.4rem;
    background: var(--global-bg-color, #1b1b1e);
    color: #9ca3af;
    text-decoration: underline dotted;
    cursor: pointer;
    font-size: 1rem;
  }
  .teaching-readmore.static {
    position: static;
    display: inline-block;
    margin-top: 0.3rem;
    background: none;
    padding-left: 0;
  }
</style>

{% assign courses_by_university = site.teachings | group_by: "university" %}
{% for group in courses_by_university %}
  <div class="teaching-group">
    <div class="teaching-university">{{ group.name }}</div>
    {% assign certificates = group.items | where: "teaching_type", "certificate" %}
{% assign courses = group.items | where_exp: "item", "item.teaching_type != 'certificate'" %}

{% assign sorted_courses = courses | sort: "year" | reverse %}
{% assign sorted_certificates = certificates | sort: "year" | reverse %}

<div class="teaching-course-row">

  {% for course in sorted_courses %}
    <div class="teaching-course">
      <a href="{{ course.url | relative_url }}" class="teaching-course-title">{{ course.title }}</a>

      <div class="teaching-course-meta">
        {{ course.term }} {{ course.year }}
        {% if course.instructor %} · {{ course.instructor }}{% endif %}
      </div>

      <div class="teaching-course-desc-wrapper">
        <p class="teaching-course-desc">{{ course.description }}</p>
        <span class="teaching-readmore" style="display: none;">Read more</span>
      </div>
    </div>
  {% endfor %}

  {% for certificate in sorted_certificates %}
    <div class="teaching-course">
      <a href="{{ certificate.url | relative_url }}" class="teaching-course-title">{{ certificate.title }}</a>

      <div class="teaching-course-meta">
        {{ certificate.term }} {{ certificate.year }}
        {% if certificate.instructor %} · {{ certificate.instructor }}{% endif %}
      </div>

      <div class="teaching-course-desc-wrapper">
        <p class="teaching-course-desc">{{ certificate.description }}</p>
        <span class="teaching-readmore" style="display: none;">Read more</span>
      </div>
    </div>
  {% endfor %}
</div>
    <!-- {% assign sorted_courses = group.items | sort: "year" | reverse %}
    <div class="teaching-course-row">
      {% for course in sorted_courses %}
        <div class="teaching-course">
          <a href="{{ course.url | relative_url }}" class="teaching-course-title">{{ course.title }}</a>
          <div class="teaching-course-meta">
            {{ course.term }} {{ course.year }}
            {% if course.instructor %} · {{ course.instructor }}{% endif %}
          </div>
          <div class="teaching-course-desc-wrapper">
            <p class="teaching-course-desc">{{ course.description }}</p>
            <span class="teaching-readmore" style="display: none;">Read more</span>
          </div>
        </div>
      {% endfor %}
    </div> -->
  </div>
{% endfor %}
<!-- {% include courses.liquid %} -->

<script>
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.teaching-course').forEach(function (card) {
      const desc = card.querySelector('.teaching-course-desc');
      const btn = card.querySelector('.teaching-readmore');
      if (!desc || !btn) return;

      if (desc.scrollHeight > desc.clientHeight + 2) {
        btn.style.display = 'inline-block';
        btn.addEventListener('click', function () {
          const expanded = desc.classList.toggle('expanded');
          if (expanded) {
            btn.textContent = 'Read less';
            btn.classList.add('static'); // once expanded, drop the overlay positioning
          } else {
            btn.textContent = 'Read more';
            btn.classList.remove('static');
          }
        });
      }
    });
  });
</script>
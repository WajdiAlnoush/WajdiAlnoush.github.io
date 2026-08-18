---
layout: page
permalink: /teaching/
title: Teaching
description: Course materials, schedules, and resources for classes taught.
nav: true
nav_order: 3
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

  .teaching-course-desc {margin: 0.5rem 0 0; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;}
  .teaching-course-desc.expanded {display: block; -webkit-line-clamp: unset; overflow: visible;}
  .teaching-readmore {display: inline-block; margin-top: 0.4rem; font-size: 0.85rem; color: var(--global-theme-color, #4fc3f7); cursor: pointer;
    background: none; border: none; padding: 0; font-weight: 600;}
</style>

{% assign courses_by_university = site.teachings | group_by: "university" %}
{% for group in courses_by_university %}
  <div class="teaching-group">
    <div class="teaching-university">{{ group.name }}</div>
    {% assign sorted_courses = group.items | sort: "year" | reverse %}
    <div class="teaching-course-row">
      {% for course in sorted_courses %}
        <div class="teaching-course">
          <a href="{{ course.url | relative_url }}" class="teaching-course-title">{{ course.title }}</a>
          <div class="teaching-course-meta">
            {{ course.term }} {{ course.year }}
            {% if course.instructor %} · {{ course.instructor }}{% endif %}
          </div>
          <p>{{ course.description }}</p>
        </div>
      {% endfor %}
    </div>
  </div>
{% endfor %}
<!-- {% include courses.liquid %} -->

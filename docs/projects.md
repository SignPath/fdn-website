---
layout: default
header: Projects
---

<ul class='projects'>
{%- for project in site.data.projects -%}
  <li><a href='/projects/{{ project.id }}'>{{ project.title }}</a> - {{ project.tagline }}</li>
{%- endfor -%}
</ul>
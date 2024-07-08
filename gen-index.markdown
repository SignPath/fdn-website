---
layout: default
---

{%- assign sprojects = site.data.projects | sort_natural: "title" -%}
{%- for project in sprojects -%}
* [**{{ project.title }}** - {{ project.tagline }}](projects/{{ project.id }})
{% endfor %}

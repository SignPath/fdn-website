---
layout: default
---

{%- for project in site.data.projects -%}
* [{{ project.title }} - {{ project.tagline }}](projects/{{ project.id }})
{% endfor %}

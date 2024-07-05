---
layout: default
---

{%- for project in site.data.projects | sort: "title" -%}
* [{{ project.title }} - {{ project.tagline }}](projects/{{ project.id }})
{% endfor %}

---
layout: default
header: Projects
---

<div class='projects-select-ctn'>
  <div>
    Search
    <input id='projects-search-field' title='Search' type='search' placeholder='Search' />
  </div>
  <div>
    Category 
    <select id='projects-category-select'>
      <option value='all'>All categories</option>
      <option value='accessability'>Accessability</option>
      <option value='audio'>Audio</option>
      <option value='developer-tools'>Developer tools</option>
      <option value='educational'>Educational</option>
      <option value='gaming'>Gaming</option>
      <option value='graphics'>Graphics</option>
      <option value='productivity'>Productivity</option>
      <option value='science'>Science</option>
      <option value='other'>Other</option>
    </select>
  </div>
</div>

<ul class='projects'>
{%- for project in site.data.projects -%}
  <li title='{{ project.title }}' data-category='{{ project.category }}'><a href='/projects/{{ project.id }}'>{{ project.title }}</a> - {{ project.tagline }}</li>
{%- endfor -%}
</ul>
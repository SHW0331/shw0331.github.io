---
layout: default
title: python
nav_order: 4
has_children: true
permalink: /docs/python
---

# Python
본 문서는 python 공식 문서를 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

- Python Version : 3.10.11

---

## Built-in functions
{% assign built_in_docs = site.pages | where: "category", "bulit-in" | sort: "title" %}
<ul>
  {% for doc in built_in_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---

## Framework
{% assign etc_docs = site.pages | where: "category", "etc" | sort: "title" %}
<ul>
  {% for doc in etc_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
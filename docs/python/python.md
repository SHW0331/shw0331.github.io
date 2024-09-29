---
layout: default
title: python
nav_order: 1
has_children: true
permalink: /docs/python
---

# Python
본 문서는 python 공식 문서를 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

- Python Version : 3.10.11

## Python built-in functions
{% assign built_in_docs = site.pages | where: "categiry", "bulit-in" | sort: "title" %}
<ul>
  {% for doc in built_in_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>
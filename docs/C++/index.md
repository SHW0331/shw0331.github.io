---
layout: default
title: c++
nav_order: 2
has_children: true
permalink: /docs/c++
---

# C++
{: .no_toc}

본 문서는 C++ 이론과 실습을 기반으로 작성되었습니다.
{: .fs-6 .fw-300 }

---

## functions
{% assign built_in_docs = site.pages | where: "category", "std-lib" | sort: "title" %}
<ul>
  {% for doc in built_in_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---

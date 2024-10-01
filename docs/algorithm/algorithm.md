---
layout: default
title: algorithm
nav_order: 3
has_children: true
permalink: /docs/algorithm
---

# Algorithm
본 문서는 algorithm의 정의와 원리를 설명하고, 예제 코드와 실습을 통해 명확히 이해하고, 실전에서 자주 등장하는 코딩 테스트 문제를 분석합니다.
{: .fs-6 .fw-300 }

---

## sort
{% assign algorithm_docs = site.pages | where: "category", "sort" | sort: "title" %}
<ul>
  {% for doc in algorithm_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

## etc
{% assign algorithm_docs = site.pages | where: "category", "etc" | sort: "title" %}
<ul>
  {% for doc in algorithm_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---


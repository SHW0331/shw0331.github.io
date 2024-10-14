---
layout: default
title: reversing
nav_order: 1
has_children: true
permalink: /docs/reversing
---

# Reversing
{: .no_toc}

본 문서는 Dreamhack 워게임 문제를 기반으로 작성되었으며, 이를 통해 도출된 분석과 해결 과정을 정리하였습니다.
{: .fs-6 .fw-300 }

---

## 기초 리버싱
{% assign basic_docs = site.pages | where: "category", "basic" | sort: "title" %}
<ul>
  {% for doc in basic_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

## 워게임 (reversing)
{% assign wargame_docs = site.pages | where: "category", "wargame" | sort: "title" %}
<ul>
  {% for doc in wargame_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
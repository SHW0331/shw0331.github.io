---
title: wargame
nav_order: 1
parent: reversing
has_children: true
---

# Reversing
{: .no_toc}

본 문서는 리버스 엔지니어링 이론과 실습을 기반으로 작성되었습니다
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
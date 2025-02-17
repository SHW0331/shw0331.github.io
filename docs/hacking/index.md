---
layout: default
title: hacking
nav_order: 3
has_children: true
permalink: /docs/hacking
---

# hacking
{: .no_toc}

본 문서는 워게임 hacking 실습을 기반으로 작성되었습니다.
{: .fs-6 .fw-300 }

---

## webhacking wargame
{% assign webhacking_docs = site.pages | where: "category", "web-hacking" | sort: "title" %}
<ul>
  {% for doc in webhacking_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---

## reversing wargame
{% assign reversing_docs = site.pages | where: "category", "reversing-hacking" | sort: "title" %}
<ul>
  {% for doc in reversing_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---


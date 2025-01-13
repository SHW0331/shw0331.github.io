---
layout: default
title: reversing
nav_order: 5
has_children: true
permalink: /docs/reversing
---

# Reversing
{: .no_toc}

본 문서는 리버스 엔지니어링 이론과 실습을 기반으로 작성되었습니다.
{: .fs-6 .fw-300 }

---

## 워게임 (reversing)
{% assign wargame_docs = site.pages | where: "category", "wargame" | sort: "title" %}
<ul>
  {% for doc in wargame_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
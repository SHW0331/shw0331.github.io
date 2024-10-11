---
layout: default
title: reversing
nav_order: 1
has_children: true
permalink: /docs/reversing
---

# Reversing
{: .no_toc}

본 문서는 "리버싱 핵심원리" 문서를 참고하여 작성하였습니다.
{: .fs-6 .fw-300 }

---

## 기초 리버싱
{% assign basic_docs = site.pages | where: "category", "basic" | sort: "title" %}
<ul>
  {% for doc in basic_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
title: Theory
nav_order: 1
parent: reversing
has_children: true
---

# Reversing
{: .no_toc}

본 문서는 "리버싱 핵심원리" 문서를 참고하여 작성하였습니다.
{: .fs-6 .fw-300 }

---

## 설명
{: .no_toc}

- 이 페이지는 리버스 엔지니어링 이론에 대해 학습하고 정리한 내용입니다. 

---

## 기초 리버싱
{% assign basic_docs = site.pages | where: "category", "basic" | sort: "title" %}
<ul>
  {% for doc in basic_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
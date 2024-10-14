---
title: wargame
nav_order: 2
parent: reversing
has_children: true
---

# Reversing
{: .no_toc}

본 문서는 리버스 엔지니어링 이론과 실습을 기반으로 작성되었습니다
{: .fs-6 .fw-300 }

## 설명
{: .no_toc}

[Dreanhack][dreamhack]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}
- 이 페이지는 리버스 엔지니어링 이론에 대해 학습하고 정리한 내용입니다. 


---

## 워게임 (reversing)
{% assign wargame_docs = site.pages | where: "category", "wargame" | sort: "title" %}
<ul>
  {% for doc in wargame_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---

[dreamhack]: https://dreamhack.io/
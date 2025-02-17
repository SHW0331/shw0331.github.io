---
title: reversing-hacking 
nav_order: 2
parent: hacking
has_children: true
category: reversing-hacking
permalink: /docs/hacking/reversing
---

# Reversing - Wargame
{: .no_toc}

본 문서는 reversing 문제를 기반으로 작성되었습니다.
{: .fs-6 .fw-300 }

## 설명
{: .no_toc}

- [Dreanhack][dreamhack]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}
- 본 문서는 리버스 엔지니어링 관련 워게임 문제를 직접 해결한 후, 도출한 해답과 실제 정답 간의 차이를 비교 분석한 내용 
- 이를 통해 해결 과정의 문제점과 개선 사항을 체계적으로 정리

---

## reversing wargame
{% assign wargame_docs = site.pages | where: "category", "reversing-wargame" | sort: "title" %}
<ul>
  {% for doc in wargame_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---

[dreamhack]: https://dreamhack.io/
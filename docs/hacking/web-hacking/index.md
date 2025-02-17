---
title: web-hacking
nav_order: 1
parent: hacking
has_children: true
category: web-hacking
permalink: /docs/hacking/web-hacking
---

# Web Hacking 
{: .no_toc}

본 문서는 Web Hacking 워게임 문제를 직접 분석하고 해결하는 과정을 정리했습니다.
{: .fs-6 .fw-300 }

## 설명
{: .no_toc}

- [Dreanhack][dreamhack]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}
- 본 문서는 웹해킹 관련 워게임 문제를 직접 해결한 후, 도출한 해답과 실제 정답 간의 차이를 비교 분석한 내용 
- 이를 통해 해결 과정의 문제점과 개선 사항을 체계적으로 정리

---

## Web Hacking - Cookie
{% assign basic_docs = site.pages | where: "category", "Cookie" | sort: "title" %}
<ul>
  {% for doc in basic_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
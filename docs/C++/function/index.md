---
title: function
nav_order: 1
parent: c++
has_children: true
---

# functions
본 문서는 C++ 공식 문서를 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

- C++ Standard Version : -

---

## 설명
{: .no_toc}

- 이 페이지는 C++ 프로그램에서 자주 사용되는 기본 함수들의 역할과 사용 방법을 이해, 학습하고 정리한 내용입니다.

---

## Standard Library Functions
{% assign std_lib_docs = site.pages | where: "category", "std-lib" | sort: "title" %}
<ul>
  {% for doc in std_lib_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
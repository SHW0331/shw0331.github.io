---
title: Function
nav_order: 1
parent: python
has_children: true
---

# Built-in functions
{: .no_toc}

본 문서는 python 공식 문서를 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

---

## 설명
{: .no_toc}

- 이 페이지는 이 페이지는 Python 기본 함수에 대해 학습하고 정리한 내용입니다.

{: .no_toc}
> Python의 **Built-in Functions(내장 함수)**는 별도의 라이브러리를 추가로 설치하거나 임포트하지 않아도 바로 사용할 수 있는 함수. 
> Python의 표준 라이브러리에 포함된 이 함수들은 개발자의 작업을 단순화하고, 효율적인 코드를 작성할 수 있도록 다양한 기능을 제공

---

## Built-in functions
{% assign built_in_docs = site.pages | where: "category", "bulit-in" | sort: "title" %}
<ul>
  {% for doc in built_in_docs %}
    <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
  {% endfor %}
</ul>

---
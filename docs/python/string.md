---
layout: default
title: string
category: "bulit-in"
parent: python
nav_order: 4
---

# 문자열 처리
{: .no_toc}

본 문서는 python docs 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

[json Docs][python json docs]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}

1. TOC
{:toc}

---

## 문자열 처리
Python 연산자는 여러 종류의 연산 작업을 수행하는 데 사용되며, 기본적인 산술 연산부터 논리적 비교, 비트 연산까지 다양한 종류가 있다. 또한, 이러한 연산자와 관련된 내장 함수들이 존재하여 연산을 좀 더 쉽게 처리할 수 있다.

## Python 문자열 처리 함수 요약

| 함수명               | 설명                                                      | 사용 예시                                       |
|----------------------|----------------------------------------------------------|-----------------------------------------------|
| `len()`              | 문자열의 길이(문자 개수)를 반환                              | `len("hello")  # 결과: 5`                      |
| `str()`              | 객체를 문자열로 변환                                        | `str(123)  # 결과: '123'`                      |
| `format()`           | 문자열 포매팅을 통해 값을 삽입하거나, 형식을 지정              | `"Hello, {}".format("world")  # 결과: 'Hello, world'` |
| `upper()`            | 문자열을 모두 대문자로 변환                                 | `"hello".upper()  # 결과: 'HELLO'`             |
| `lower()`            | 문자열을 모두 소문자로 변환                                 | `"HELLO".lower()  # 결과: 'hello'`             |
| `strip()`            | 문자열 양쪽 끝의 공백이나 특정 문자 제거                     | `"  hello  ".strip()  # 결과: 'hello'`         |
| `split()`            | 구분자를 기준으로 문자열을 나눠 리스트로 반환                 | `"a,b,c".split(',')  # 결과: ['a', 'b', 'c']`  |
| `join()`             | 리스트 등의 iterable을 문자열로 결합                         | `",".join(['a', 'b', 'c'])  # 결과: 'a,b,c'`   |
| `replace()`          | 문자열 내의 특정 부분을 다른 문자열로 대체                   | `"hello".replace("l", "x")  # 결과: 'hexxo'`   |
| `find()`             | 문자열 내에서 특정 문자나 문자열의 첫 번째 위치를 반환         | `"hello".find('e')  # 결과: 1`                 |
| `count()`            | 문자열 내에서 특정 문자의 출현 횟수를 반환                    | `"hello".count('l')  # 결과: 2`                |

---

[python json docs]: https://docs.python.org/3/tutorial/index.html
---
layout: default
title: operator
category: "bulit-in"
parent: python
nav_order: 2
---

# 연산자
{: .no_toc}

본 문서는 python docs 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

[json Docs][python json docs]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}

1. TOC
{:toc}

---

## 연산자
Python 연산자는 여러 종류의 연산 작업을 수행하는 데 사용되며, 기본적인 산술 연산부터 논리적 비교, 비트 연산까지 다양한 종류가 있다. 또한, 이러한 연산자와 관련된 내장 함수들이 존재하여 연산을 좀 더 쉽게 처리할 수 있다.

## Python 연산자 요약

| 함수명               | 설명                                                        | 사용 예시                                       |
|----------------------|-------------------------------------------------------------|------------------------------------------------|
| `abs()`              | 주어진 숫자의 절대값을 반환하는 함수                           | `absolute_value = abs(-5)  # 결과: 5`           |
| `divmod()`           | 두 숫자의 몫과 나머지를 튜플로 반환하는 함수                    | `result = divmod(10, 3)  # 결과: (3, 1)`        |
| `pow()`              | 거듭제곱을 계산하는 함수 (`x**y`와 동일)                      | `result = pow(2, 3)  # 결과: 8`                 |
| `round()`            | 주어진 숫자를 소수점 자리에서 반올림하는 함수                  | `rounded = round(3.14159, 2)  # 결과: 3.14`     |
| `sum()`              | iterable(리스트 등)에 있는 값들의 합을 계산하는 함수            | `total = sum([1, 2, 3, 4])  # 결과: 10`         |
| `min()`              | 주어진 iterable 또는 여러 인자 중 최소값을 반환하는 함수        | `smallest = min(3, 1, 2)  # 결과: 1`            |
| `max()`              | 주어진 iterable 또는 여러 인자 중 최대값을 반환하는 함수        | `largest = max(3, 1, 2)  # 결과: 3`             |
| `any()`              | 주어진 iterable 내의 요소 중 하나라도 참(True)이면 참을 반환     | `result = any([False, True, False])  # 결과: True` |
| `all()`              | 주어진 iterable 내의 모든 요소가 참(True)이면 참을 반환         | `result = all([True, True, False])  # 결과: False` |


## abs(0)


```py
user_input = input("input : ")
print(f'input() : {user_input}')
# 입력 값 : shw98
# 출력 값 : input() : shw98
```

---
[python json docs]: https://docs.python.org/3/tutorial/index.html
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

## len()
`len()` 함수는 iterable 객체의 길이를 반환하는 함수이다. 여기서 길이는 해당 객체에 포함된 요소의 개수를 의미

```py
numbers = [1, 2, 3, 4, 5]
result = len(numbers)
print(f'list len : {result}') # list len : 5

text = 'shw0331'
result = len(text)
print(f'string len : {result}') # string len : 7

data_dict = {'a': 1, 'b':2, 'c':3}
result = len(data_dict)
print(f'dict len : {result}') # dict len : 3
```

## enumerate()
`enumerate()` 함수는 주어진 iterable을 열거형으로 만들어 각 요소와 함께 인덱스를 반환하는 함수이다. 이를 통해 루프를 돌면서 인덱스와 값을 동시에 사용할 수 있다.

{: .no_toc}
> **start** 옵션을 추가하여 인덱스 시작 값을 설정할 수 있다.
> `enumerate(iterable, start=1), 시작 값 1

```py
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(f'과일 {index} : {fruit}') 
    # 과일 1 : apple
    # 과일 2 : banana
    # 과일 3 : cherry

data_tuple = ('a', 'b', 'c')
for index, value in enumerate(data_tuple):
    print(f'index {index} : {value}')
    # index 0 : a
    # index 1 : b
    # index 2 : c
```

## zip()
`zip()` 함수는 여러 iterable 객체의 요소들을 같은 인덱스끼리 묶어 튜플로 반환하는 함수이다. 각 iterable에서 동일한 인덱스에 위치한 요소들을 하나의 튜플로 묶고, 그 튜플들의 리스트(또는 다른 iterable)를 반환한다.

{: .no_toc}
> | 차이점        | **튜플 (tuple)**                                | **리스트 (list)**                             |
> |---------------|-------------------------------------------------|-----------------------------------------------|
> | **가변성**    | 불변(immutable): 한 번 생성되면 값을 변경할 수 없음. | 가변(mutable): 값을 추가, 수정, 삭제할 수 있음. |
> | **표현 방식** | 소괄호 `()`로 표현                               | 대괄호 `[]`로 표현                             |
> | **사용 목적** | 변경할 필요 없는 데이터를 저장할 때 사용            | 데이터 수정, 추가, 삭제가 필요한 경우 사용       |
> | **메모리 사용**| 리스트보다 더 적은 메모리를 사용                    | 튜플보다 더 많은 메모리를 사용                  |
> | **속도**      | 튜플이 리스트보다 빠름                             | 리스트는 튜플보다 상대적으로 느림               |
> | **메서드**    | 소수의 메서드만 제공 (`count()`, `index()` 등)      | 다양한 메서드 제공 (`append()`, `extend()`, `remove()` 등) |
> | **사용 용도** | 데이터를 보호하고 싶을 때, 변경이 불필요한 경우에 사용 | 데이터를 변경, 수정, 추가해야 할 때 사용         |


---

[python json docs]: https://docs.python.org/3/tutorial/index.html
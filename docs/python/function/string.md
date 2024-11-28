---
layout: default
title: string
category: "bulit-in"
parent: Function
nav_order: 4
---

# 문자열 처리
{: .no_toc}

본 문서는 python docs 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

[Python Docs][python docs]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}

1. TOC
{:toc}

---

## 문자열 처리
Python 연산자는 여러 종류의 연산 작업을 수행하는 데 사용되며, 기본적인 산술 연산부터 논리적 비교, 비트 연산까지 다양한 종류가 있다. 또한, 이러한 연산자와 관련된 내장 함수들이 존재하여 연산을 좀 더 쉽게 처리할 수 있다.

## Python 문자열 처리 함수 요약

| 함수명               | 설명                                                      | 사용 예시                                     |
|----------------------|----------------------------------------------------------|----------------------------------------------|
| `len()`              | 문자열의 길이(문자 개수)를 반환                              | `len("hello")  # 결과: 5`                    |
| `str()`              | 객체를 문자열로 변환                                        | `str(123)  # 결과: '123'`                    |
| `format()`           | 문자열 포매팅을 통해 값을 삽입하거나, 형식을 지정              | `"Hello, {}".format("world")  # 결과: 'Hello, world'` |
| `upper()`            | 문자열을 모두 대문자로 변환                                 | `"hello".upper()  # 결과: 'HELLO'`           |
| `lower()`            | 문자열을 모두 소문자로 변환                                 | `"HELLO".lower()  # 결과: 'hello'`           |
| `strip()`            | 문자열 양쪽 끝의 공백이나 특정 문자 제거                     | `"  hello  ".strip()  # 결과: 'hello'`       |
| `split()`            | 구분자를 기준으로 문자열을 나눠 리스트로 반환                 | `"a,b,c".split(',')  # 결과: ['a', 'b', 'c']`|
| `join()`             | 리스트 등의 iterable을 문자열로 결합                         | `",".join(['a', 'b', 'c'])  # 결과: 'a,b,c'` |
| `replace()`          | 문자열 내의 특정 부분을 다른 문자열로 대체                   | `"hello".replace("l", "x")  # 결과: 'hexxo'` |
| `find()`             | 문자열 내에서 특정 문자나 문자열의 첫 번째 위치를 반환         | `"hello".find('e')  # 결과: 1`               |
| `count()`            | 문자열 내에서 특정 문자의 출현 횟수를 반환                    | `"hello".count('l')  # 결과: 2`              |
| `reversed()`         | 문자열을 역순으로 반환                                      | `"hello"[::-1]  # 결과: 'olleh'`             |
| `enumerate()`        | 문자열을 인덱스와 함께 열거하여 반환                        | `for idx, char in enumerate('hello'): print(idx, char)`  |
| `zip()`              | 여러 문자열을 병렬로 묶어서 튜플 형태로 반환                | `zip('abc', '123')  # 결과: [('a', '1'), ('b', '2'), ('c', '3')]` |

---

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

## str()
`str()` 함수는 객체를 문자열로 변환하는 함수이다. 숫자, 리스트, 튜플, 딕셔너리, 또는 다른 타입의 객체를 문자열로 변환할 때 사용한다.

```py
num = 980
result = str(num)
print(result) # 980
print(type(result)) # <class 'str'>

boolean_value = True
result = str(boolean_value)
print(result) # True
print(type(result)) # <class 'str'>
```

## format()
`format()` 함수는 문자열을 포맷팅하여 특정 값이나 데이터를 삽입하거나, 형식을 지정하는 데 사용한다.

```py
result = 'Test, {}'.format('format() 테스트')
print(result) # Test, format() 테스트
```

## upper()
`upper()` 함수는 문자열의 모든 문자를 대문자로 변환한다.

```py
result = 'shw'.upper()
print(result) # SHW
```

## lower()
`lower()` 함수는 문자열의 모든 문자를 소문자로 변환한다.

```py
result = 'SHW'.lower()
print(result) # shw
```

## strip()
`strip()` 함수는 문자열 양쪽 끝의 공백 또는 특정 문자를 제거한다. 기본적으로 공백을 제거하며, 특정 문자를 지정할 수도 있다.

```py
result = '     space    '.strip()
print(result) # space

result = '#######space#########'.strip('#')
print(result) # space
```

## split()
`split()` 함수는 문자열을 특정 구분자를 기준으로 나누어 리스트로 반환한다. 기본 구분자는 공백이며, 다른 구분자를 지정할 수 있다.

```py
result = 'a,b,c'.split(',')
print(result) # ['a', 'b', 'c']

result = 'abc de fgh ijk'.split()
print(result) # ['abc', 'de', 'fgh', 'ijk']
```

## join()
`join()` 함수는 리스트나 iterable의 요소를 하나의 문자열로 결합할 때 사용한다. 요소 사이에 구분자를 넣어 결합할 수 있다.

```py
result = ','.join(['a', 'b', 'c'])
print(result) # a,b,c

result = ' '.join(['aaaaaaa', 'bbbbb'])
print(result) # aaaaaaa bbbbb
```

## replace()
`replace()` 함수는 문자열 내의 특정 부분을 다른 문자열로 대체하는 함수이다. 문자열의 모든 해당 부분이 바뀐다.

```py
result = 'shw98'.replace('98', '0331')
print(result) # shw0331
```

## find()
`find()` 함수는 문자열 내에서 특정 문자나 문자열의 첫 번째 위치를 반환한다. 찾는 문자가 없으면 **-1**을 반환한다.

```py
result = 'shw0331'.find('s')
print(result) # 0 : index 0

result = 'shw0331'.find('w')
print(result) # 2 : index 2

result = 'shw0331'.find('a')
print(result) # -1 : False
```

## count()
`count()` 함수는 문자열 내에서 특정 문자가 몇 번 등장하는지 출현 횟수를 반환한다.

```py
result = 'shw0331'.count('3')
print(result) # 2

result = 'shw0331'.count('a')
print(result) # 0
```

## reversed()
`reversed()` 함수는 주어진 iterable 객체의 요소들을 역순으로 반환하는 함수이다. 이 함수는 원본 데이터를 변경하지 않고, 역순으로 iterator를 반환한다.

{: no_toc }
> `reversed()` 함수는 문자열을 뒤집은 값을 바로 반환하는 것이 아니라, **reversed object**라는 **iterator**를 반환합니다. 이 iterator 원래의 문자열을 거꾸로 순회할 수 있는 객체이지만, 이를 바로 출력하면 사람이 읽을 수 있는 문자열 형태로 출력되지 않습니다.

```py
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reversed(numbers)
print(list(reversed_numbers)) # [5, 4, 3, 2, 1]

text = 'shw0331'
reversed_text = reversed(text)
print(''.join(reversed_text)) # 1330whs
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

```py
names = ['shw', 'abc', 'qwe']
ages = [27, 33, 12]
result = zip(names, ages)
print(result)
# index 0 : a
# index 1 : b
# index 2 : c
print(list(result)) # [('shw', 27), ('abc', 33), ('qwe', 12)]

teams = ['a', 'b', 'c']
scores = [5, 7, 2]
result = zip(teams, scores)
for team, score in result:
    print(f'{team} : {score}점')
    # a : 5점
    # b : 7점
    # c : 2점
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

---

[python docs]: https://docs.python.org/3/tutorial/index.html
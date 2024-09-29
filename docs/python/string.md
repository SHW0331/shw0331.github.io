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


## 기본 산술 연산자(Arithmetic Operators)
산술 연산을 수행하는 연산자
- `+` : 덧셈 연산
- `-` : 뺄셈 연산
- `*` : 곱셈 연산
- `/` : 나눗셈 연산 (소수점 포함)
- `//` : 나눗셈 연산 (소수점 버림)
- `%` : 나머지 연산
- `**` : 거듭제곱 연산

```py
# 변수 선언
x = 9
y = 8

# 덧셈 연산
result = x + y
print(f'X + Y = {result}') # X + Y = 17

# 뺄셈 연산
result = x - y
print(f'X - Y = {result}') # X - Y = 1

# 곱셈 연산
result = x * y
print(f'X * Y = {result}') # X * Y = 72

# 나눗셈 연산 (소수점 포함)
result = x / y
print(f'X / Y = {result}') # X / Y = 1.125

# 나눗셈 연산 (소수점 미포함)
result = x // y
print(f'X // Y = {result}') # X // Y = 1

# 나머지 연산
result = x % y
print(f'X % Y = {result}') # X % Y = 1

# 거듭제곱 연산
result = x ** y
print(f'X ** Y = {result}') # X ** Y = 43046721
```

## abs()
`abs`는 숫자의 절대값을 반환하는 함수이다. 절대값이란 음수값을 양수로 바꿔주는 것이며, 양수와 0은 그대로 반환

```py
x = -9
print(abs(x)) # 9
print(abs(-x)) # 9

y = -8.31
print(abs(y)) # 8.31
print(abs(-y)) # 8.31
```

## divmod()
`divmod()`는 두 숫자를 나누어 몫과 나머지를 한 번에 계산하고 결과 값을 **tuple** 형태로 반환

{: .no_toc}
>**tuple**이란 여러 개의 값을 순서가 있는 형태로 저장할 수 있는 자료구조이다. **tuple**은 immutable(불변), 즉 한 번 생성되면 그 안의 요소를 변경하거나 추가할 수 없다.

```py
result = divmod(10, 3)
print(result) # (3, 1)

# 몫과 나머지를 각각 변수로 저장
quotient, remainder = divmod(9.5, 2)
print(f'quotient : {quotient}, remainder : {remainder}') # quotient : 4.0, remainder : 1.5
```

## pow()
`pow()`는 거듭제곱을 계산하는 함수로, 기본적인 두 인자를 사용한 거듭제곱뿐만 아니라 세 번째 인자를 사용하여 모듈러 연산도 지원한다. `pow()`는 매우 큰 숫자들의 연산이 필요할 때 사용하면 효율적인 모듈러 연산을 수행할 수 있다.

{: .no_toc}
>**모듈러 연산**이란, 어떤 수를 다른 수로 나누고 그 나머지를 구하는 연산, 나머지 연산이라고도 불린다.
>예시 : `a % b = r`이면, `a = bq + r`로 나타낼 수 있다, 여기서 `q`는 몫, `r`은 나머지, `r`은 항상 `0 <= r < b` 범위에 있다.

```py
# 두 인자 : **
result = pow(2, 3)
print(result) # 8

# 세 번째 인자 지정 : (base ** exp) % mod
# base: 밑, exp: 지수, %: 모듈러 연산
result = pow(2, 3, 5) # (2 ** 3) % 5
print(result) # 3
```

## round()
`round()`는 주어진 숫자를 지정한 소수점 자릿수에 맞춰 반올림하는 함수이다. 선택적으로 몇 번째 소수점 자리에서 반올림할지 지정할 수 있다.

{: .no_toc}
>`round()` 함수의 "은행가 반올림"(Banker's Rounding) 방식은 0.5와 같은 정확히 중간 값이 나올 때 짝수 방향으로 반올림하는 규칙입니다. 이 방식은 수학적으로 **"가장 가까운 짝수"**로 반올림하는 방식을 의미
> ```py
> print(round(0.5))  # 0 (짝수인 0으로 반올림)
> print(round(1.5))  # 2 (짝수인 2로 반올림)
> print(round(2.5))  # 2 (짝수인 2로 반올림)
> print(round(3.5))  # 4 (짝수인 4로 반올림)
> print(round(4.5))  # 4 (짝수인 4로 반올림)
> ```

```py
x = 3.141592
y = round(x, 2) # 2(ndigits) : 2자리 소수점 이하 자릿수 반올림
print(y) # 3.14

z = round(y, 1)
print(z) # 3.1

k = round(z) # ndigits 생략하면 소수점 아래를 없애고 가장 가까운 정수로 반올림
print(k) # 3
```

## sum()
`sum()`은 **iterable**의 모든 요소의 합을 계산하는 함수이다. 대표적인 **iterable**로는 list, tuple, set, dictionary가 있다.

{: .no_toc}
> **iterable**은 반복할 수 있는 객체로, 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 포함된다. 이 객체들은 `for` 루프나 다른 반복 작업에서 순차적으로 하나씩 요소에 접근할 수 있다.

```py
# list의 모든 요소 합
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result) # 15

# tuple의 모든 요소 합
numbers = (1, 2, 3, 4, 5)
result = sum(numbers)
print(result) # 15

# start 인자를 사용하여 합산
numbers = [1, 2, 3]
result = sum(numbers, 10) # start : 10
print(result) # 16
```

## min()
`min()`은 iterable 또는 여러 개의 인자에서 가장 작은 값을 반환한다.

```py
numbers = [4, 1, 7, 3]
result = min(numbers)
print(result) # 1

result = min(4, 1, 7, 3)
print(result) # 1

result = min('python') # 문자열의 경우, 사전 순서로 가장 앞에 있는 문자를 반환
print(result) # h
```

## max()
`max()`는 iterable에서 가장 큰 값을 반환하는 함수이다.

```py
numbers = [5, 8, 2, 9, 12, 4]
result = max(numbers)
print(result) # 12

# key 매개변수에서 max() 사용 : 가장 긴 문자열 출력
words = ["Python", "Java", "C++"]
print(max(words, key=len)) # Python
```

## all()
`all()`은 iterable에서 모든 요소가 참인지 확인하는 함수이다. 모든 요소가 참일 경우 **True**를 반환하며, 하나라도 거짓이 포함되어 있으면 **False**를 반환한다.

```py
numbers = [1, 2, 3, 4, 5]
result = all(numbers)
print(result) # True

numbers = [1, 2, 3, 4, 0]
result = all(numbers)
print(result) # False, 0은 거짓

empty_list = [ ]
result = all(empty_list)
print(result) # True, 빈 리스트나, 빈 튜플은 결과가 항상 True
```

## any()
`any()`는 주어진 iterable에서 하나라도 **True**값이 있을 때 **True**를 반환하는 함수이다. 모든 값이 **False**이면 False를 반환한다.

```py
numbers = [0, 1, 0, 0]
result = any(numbers)
print(result) # True

numbers = [0, 0, 0, 0]
result = any(numbers)
print(result) # False

empty_list = [ ]
result = any(empty_list)
print(result) # Flase
```

---
[python json docs]: https://docs.python.org/3/tutorial/index.html
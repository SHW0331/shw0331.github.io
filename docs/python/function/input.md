---
layout: default
title: input
category: "bulit-in"
parent: function
nav_order: 2
---

# 사용자 입력 함수
{: .no_toc}

본 문서는 python docs 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

[Python Docs][python docs]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}

1. TOC
{:toc}

---

## 사용자 입력 함수
파이썬에서 사용자 입력을 받을 수 있는 다양한 함수들이 있다. 기본적인 입력 함수부터 특수한 경우에 사용할 수 있는 함수도 있다.

## Python 사용자 입력 함수 요약

| 함수명                | 설명                                                      | 사용 예시                                 |
|----------------------|----------------------------------------------------------|------------------------------------------|
| `input()`            | 기본적인 문자열 입력 함수                                      | `name = input("이름을 입력하세요")`         |
| `sys.stdin.read()`    | 여러 줄 입력을 받을 때 사용, EOF까지 모든 데이터를 읽음                         | `data = sys.stdin.read()`                |
| `getpass.getpass()`   | 비밀번호 등 민감한 입력을 받을 때 사용, 화면에 입력 내용이 표시되지 않음               | `password = getpass.getpass("비밀번호")`    |
| `argparse`           | 명령줄 인자를 처리하는 데 사용                                   | `parser = argparse.ArgumentParser()`     |
| `fileinput.input()`   | 여러 파일이나 표준 입력에서 한 줄씩 입력을 읽음                              | `for line in fileinput.input(): print(line)` |

---

## input()
가장 기본적인 사용자 입력 함수로, 사용자로부터 한 줄의 입력을 받을 때 사용, 입력된 값은 항상 문자열로 반환

```py
user_input = input("input : ")
print(f'input() : {user_input}')
# 입력 값 : shw98
# 출력 값 : input() : shw98
```

## sys.stdin.read()
`sys.stdin.read()`는 여러 줄의 데이터를 받을 때 유용, 일반적으로 EOF(End of File)를 통해 입력을 종료

{: .no_toc}
> **EOF(End of File)**는 입력 스트림에서 더 이상 읽을 데이터가 없을 때 발생하며, Python에서는 표준 입력을 통해 여러 줄의 데이터를 받을 때 사용자가 입력을 종료하려면 EOF 신호를 보내야 한다.
- Windows : Ctrl + Z 를 누르고 Enter 를 누르면 EOF 신호 발생
- Unix/Linux/Mac : Ctrl + D 를 누르면 EOF 신호가 발생

```py
import sys
print("여러 줄의 텍스트를 입력하고, Ctrl+D(Unix) 또는 Ctrl+Z(Windows)로 종료")
multi_line_input = sys.stdin.read()
print(f"Sys stdin read() : \n{multi_line_input}")
# 입력 값 :
# sys sdin read Test
# python
# shw98
# ^Z

# 출력 값 : 
# Sys stdin read() : 
# sys sdin read Test
# python
# shw98
```

## getpass()
비밀번호와 같은 민감한 데이터를 입력받을 때 사용, 이 함수는 비밀번호를 입력받는 상황에서 유용하며, 사용자가 입력하는 내용을 보이지 않도록 보호

```py
import getpass
password = getpass.getpass('Password : ')
print(f'Password : {'*' * len(password)}')
# 입력 값(filtering) : 
# 출력 값 : Password : ****
# 실제 값 : Password : 1998
```

## argparse()
명령행 인자를 통해 입력을 받을 수 있는 모듈, 스크립트를 실행할 때 명령행 옵션을 지정 가능

```py
import argparse
parser = argparse.ArgumentParser(description='argparse : ')
parser.add_argument('--name', type=str, help='user name')
args = parser.parse_args()
print(f'argparser() : {args}')
# Script : python test.py --name 'shw98'
# 출력 값 : argparse() : Namespace(name='shw98')
```

## fileinput.input()
파일이나 표준 입력에서 여러 줄을 입력받을 때 사용. 주로 파일에서 데이터를 읽어올 때 유용

```py
import fileinput
for line in fileinput.input():
    print(f"line : {line.strip()}")
# Script : python test.py test.txt
# 출력 값 : 
# line : file input Test
# line : 1. python
# line : 2. shw98
# line : 3. test
```

---

[python docs]: https://docs.python.org/3/tutorial/index.html
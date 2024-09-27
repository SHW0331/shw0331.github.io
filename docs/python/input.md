---
layout: default
title: input
parent: python
nav_order: 2
---

# 사용자 입력 함수
{: .no_toc}

본 문서는 python docs 참고하여 작성되었습니다.
{: .fs-6 .fw-300 }

[json Docs][python json docs]{: .btn .fs-5 .mb-4 .mb-md-0 target="_blank"}

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
| `click.prompt()`      | 데이터 유형을 지정할 수 있는 고급 입력 함수                              | `age = click.prompt("나이", type=int)`    |
| `PyInquirer.prompt()` | 메뉴 기반의 입력 및 다중 선택 입력 처리 가능                            | `answers = prompt(questions)`            |



```

---
[python json docs]: https://docs.python.org/3/tutorial/index.html
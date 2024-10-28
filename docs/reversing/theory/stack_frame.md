---
layout: default
title: Stack Frame
nav_order: 6
category: "basic"
parent: Theory
---

# Stack Frame 기본 설명
{: .no_toc}

스택 프레임의 동작 원리를 이해
{: .fs-6 .fw-300 }

---

1. TOC
{:toc}

---

## 실습 목표
- 간단한 프로그램을 만들고 디버거를 이용해서 스택 프레임을 확인
- 간단한 어셈블리 명령어의 상세 설명

---

## 1.1 스택 프레임이란
- ESP(스택 포인터)가 아닌 EBP(베이스 포인터)레지스터를 사용하여 스택 내의 로컬 변수, 파라미터, 복귀 주소에 접근하는 기법
- ESP 레지스터가 스택 포인터 역할
- EBP 레지스터는 베이스 포인터 역할

{: .no_toc}
> - ESP 레지스터의 값은 프로그램 안에서 수시로 변경되기 때문에 스택에 저장된 변수, 파라미터에 접근하고자 할 때 ESP 값을 기준으로 하면 프로그램을 만들기 어려움
> - 따라서 어떤 기준 시점(함수 시작)의 ESP 값을 EBP에 저장하고 이를 함수 내에서 유지해주면, ESP 값이 아무리 변하더라도 EBP를 기준(base)으로 안전하게 해당 함수의 변수, 파라미터, 복귀 주소에 접근 가능

---

## 2.1 실습 예제 - stackframe.exe
- 스택 프레임의 설명을 위해 아주 간단한 프로그램을 만들어 실습
- StackFrame.cpp
```cpp
#include "stdio.h"

long add(long a, long b)
{
	long x = a, y = b;
	return (x + y);
}

int main(int argc, char* argv[])
{
	long a = 1, b = 2;
	printf("%d\n", add(a, b));
	return 0;
}

// 출력 값
// 3
```

<br>

- OllyDbg로 StackFrame.exe 파일을 열고 401000 주소로 이동
- 원본 C 소스코드와 그에 대응되는 어셈블리 코드를 하나씩 살펴보고 각 단계별로 스택의 모습을 이해
- ![](../../../assets/images/reversing/StackFrame/1.PNG)

## 2.2 main() 함수 시작 & 스택 프레임 생성
- StackFrame.cpp에서 아래 코드 부분에 해당되는 내용
```cpp
int main(int argc, char* argv[])
{
```

<br>

- 먼저 main() 함수 시작 시 스택의 상태는 

- main() 함수(401020)에 BP를 설치한 후, 실행
- 



---

{: .no_toc}
> - 스택에 값을 입력하면 스택 포인터(ESP)는 감소
> - 스택에서 값을 꺼내면 스택 포인터는 증가
> - 스택 포인터의 초기 값은 스택 메모리의 아래쪽에 있다는 특징이 있음


---

> [OllyDbg](https://www.ollydbg.de/)



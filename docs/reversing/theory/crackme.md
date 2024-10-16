---
layout: default
title: abex' crackme#1
nav_order: 5
category: "basic"
parent: Theory
---

# abex' crackme #1 분석
{: .no_toc}

간단한 crackme 샘플을 분석 및 실습
{: .fs-6 .fw-300 }

---

1. TOC
{:toc}

---

## 실습 목표
- abex' crackme #1 분석하여 디버거와 디스어셈 코드에 적응

---

## 1.1 abex' crackme #1
- 디버깅을 시작하기 전에 먼저 파일을 실행시켜서 어떤 프로그램인지 확인
- Make me think your HD is a CD-Rom, 메시지 박스가 출력
- ![](../../../assets/images/reversing/abex'%20crackme#1/1.png)

<br>

- 확인 버튼을 누르면, Nah... This is not a CD-ROM Drive! 메시지 박스가 출력
- abex' crackme 파일이 어셈블리 언어로 만들어진 실행 파일이기 때문에, EP 코드가 매우 짧음
- 어셈블리 언어로 작성하면 어셈 코드가 곧 디스어셈 코드가 된다.
- ![](../../../assets/images/reversing/abex'%20crackme#1/2.png)

{: .no_toc}
> - EP 코드는 프로그램의 엔트리 포인트(Entry Point) 코드를 의미한다. 엔트리 포인트는 운영 체제가 프로그램을 실행할 때 제어가 처음으로 넘어가는 위치 

---

## 2.1 코드 분석
- 오른쪽 상단 부분의 Win32 API 함수 호출 위주로 분석
- GetDriveType() API로 C드라이브의 타입을 얻어옴.
- 이걸 조작해서 CD-ROM 타입으로 인식하도록 만들어서 "OK, I really think that your HD is a CD-ROM! :p" 메시지 박스가 출력되도록 수정

```c
MessageBox("Make me think your HD is a CD-ROM.")
GetDriveType("C:\\")
...
MessageBox("Nah... This is not a CD-ROM Drive!")
ExitProcess()
```

## 2.2 전체 코드에서 사용된 어셈블리 명령어
- PUSH : 스택에 값을 입력
- CALL : 지정된 주소의 함수를 호출
- INC : 값을 1 증가
- DEC : 값을 1 감소
- JMP : 지정된 주소로 점프
- CMP : 주어진 두 개의 operand 비교
- JE : 조건 분기(Jump if equal)
- ![](../../../assets/images/reversing/abex'%20crackme#1/3.png)

{: .no_toc}
> - CMP는 SUB 명령어와 동일하나 operand 값이 변경되지 않고 EFLAGS 레지스터만 변경됨 (**두 operand의 값이 동일하다면 SUB 결과는 0이고 ZF = 1로 세팅**)
> - Operand는 컴퓨터 명령어에서 사용되는 데이터나 주소를 의미
> - JE는 **ZF = 1**이면 점프

---

## 3.1 크랙
- 단순 패치가 목적이라면 401026 주소 명령어(JE SHORT 0040103D)를 Assemble 기능을 이용하여 JMP SHORT 0040103D 명령어로 변경
- JE 명령어를 JMP 명령어로 바꾸는 것
- ![](../../../assets/images/reversing/abex'%20crackme#1/4.png)

---

## 4.1 스택에 파라미터를 전달하는 방법
- 401000 ~ 40100E 주소 사이의 명령어를 확인
- MessageBoxA() 함수를 호출하기 전에 4번의 PUSH 명령어를 사용하여 필요한 파라미터를 역순으로 입력


---

> [OllyDbg](https://www.ollydbg.de/)



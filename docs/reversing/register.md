---
layout: default
title: Register
nav_order: 3
category: "basic"
parent: reversing
---

# IA-32 Register 기본 설명
{: .no_toc}

IA-32(Intel Architecture 32비트) 설명
{: .fs-6 .fw-300 }

---

1. TOC
{:toc}

---

## 실습 목표
- 애플리케이션의 디버깅을 위해 기본적으로 알아야 할 IA-32의 레지스터에 대하여 분석

---

## 1.1 CPU 레지스터란?
- CPU 레지스터는 CPU 내에서 사용되는 고속 메모리 저장소이다.
- 레지스터(Register)란 CPU 내부에 존재하는 다목적 저장 공간
- CPU가 명령을 실행하거나 데이터를 처리할 때 필요한 값을 즉시 읽고 쓸 수 있는 장소로, 일반적인 메모리(RAM)보다 훨 씬 빠르게 접근할 수 있다.

## 1.2 IA-32의 레지스터
- IA-32는 **인텔 아키텍처 32비트(Intel Architecture, 32-bit)**의 약자로, x86 아키텍처의 32비트 버전을 의미
- IA-32는 지원하는 기능도 많고 그만큼 레지스터의 수도 많다.
- 애플리케이션 디버깅의 초급 단계에서는 Basic program execution register에 대해서 알아두어야 한다.

{: .no_toc}
> - Basic program execution registers
> - x87 FPU registers
> - MMX registers
> - XMM registers
> - Control registers
> - Memory management registers
> - Debug registers
> - Memory type range registers
> - Machine specific registers
> - Machine check registers
> - ...

## 1.3 Basic program execution registers
- 해당 레지스터는 프로그램 실행과 제어에 필요한 다양한 정보를 저장하고 관리하는 CPU 내 레지스터들을 의미
- Basic program execution registers는 4개의 그룹으로 나눌 수 있다.
- General Purpose Registers (32비트 - 8개)
- Segment Registers (16비트 - 6개)
- Program Status and Control Register (32비트 - 1개)
- Instruction Pointer (32비트 - 1개)
- ![](../../assets/images/reversing/Register/1.png)

## 1.4 범용 레지스터
- 범용 레지스터(General Purpose Registers)는 여러 종류의 데이터 처리를 위한 다목적 저장 공간
- 주로 산술 연산이나 논리 연산을 수행하는 데 사용되며, 각종 데이터를 임시로 저장
- IA-32에서 각각의 범용 레지스터들의 크기는 32비트(4바이트)이다.
- ![](../../assets/images/reversing/Register/2.png)

| 레지스터  | 설명                                                                 |
|-----------|----------------------------------------------------------------------|
| **EAX**   | 주로 산술 연산의 결과를 저장하는 **누산기(accumulator)**로 사용 |
| **EBX**   | 데이터를 저장하는 데 사용되는 기본 레지스터                     |
| **ECX**   | 반복 연산에서 **카운터(counter)**로 사용                         |
| **EDX**   | EAX와 함께 곱셈, 나눗셈 연산 등에서 보조적으로 사용              |
| **ESI/EDI** | 문자열 연산이나 메모리 주소 계산에 자주 사용                     |
| **EBP/ESP** | 스택 포인터와 관련된 작업을 처리. 함수 호출 시 스택에 데이터를 저장하고, 스택의 최상단을 추적하는 데 사용. |

{: .no_toc}
> - 각 레지스터들은 16비트 하위 호환을 위하여 몇 개의 구획으로 나뉜다. (EAX를 기준으로 설명)
> - EAX : (0 ~ 31) 32비트
> - AX : (0 ~ 15) EAX의 하위 16비트
> - AH : (8 ~ 15) AX의 상위 8비트
> - AL : (0 ~ 7) AX의 하위 8비트
> - 즉 4바이트(32비트)를 다 사용하고 싶을 때는 **EAX**를 사용하고, 2바이트(16비트)만을 사용할 때는 EAX의 하위 16비트 부부인 **AX**를 사용하면 된다.
> - 이런식으로 상황에 맞게 8비트, 16비트, 32비트로 알뜰하게 사용

---

> [OllyDbg](https://www.ollydbg.de/)



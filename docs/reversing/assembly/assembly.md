---
layout: default
title: assembly
parent: reversing
nav_order: 2
permalink: /docs/reversing/assembly
---

# Assembly
{: .no_toc }

1. TOC
{:toc}
---

# Assembly?

## 어셈블리어란 무엇인가?
- 최초의 프로그래밍 언어 중 하나로, 기계어의 직접적인 상위 수준 언어
- 어셈블리어는 CPU가 직접 이해할 수 있는 저수준 언어(low-level language)이다.
- 이는 기계어와 매우 밀접하게 연관되어 있으며, 특정한 기계 명령어에 대응된다.

## 어셈블리어의 특징
- 하드웨어에 매우 근접한 저수준(low-level) 프로그래밍 언어
- 컴퓨터 구조를 깊이 이해해야만 제대로 사용 가능
- 일반적으로 높은 성능과 작은 코드 크기를 제공

## 어셈블리어의 용도
- 시스템 프로그래밍 (운영체제, 드라이버 등)
- 성능 최적화가 필요한 프로그램
- 리버스 엔지니어링 및 디버깅

---
# 왜 프로그래밍 언어는 CPU가 직접 이해하지 못할까?

## Program language
- 프로그래밍 언어, 즉 고수준 프로그래밍 언어 (high-level language)
- 인간이 읽기 쉽게 작성된 언어로, 추상화 수준이 높아 복잡한 작업을 간단한 코드로 표현 가능
- 다양한 플랫폼에서 작동할 수 있도록 설계

## 컴파일러와 인터프리터
- 고수준 언어로 작성된 코드는 CPU가 직접 실행할 수 없기 때문에, 중간에 번역 과정이 필요
- 컴파일러는 전체 프로그램 코드를 기계어로 번역하여 실행 파일을 생성 (C, C++)
- 인터프리터는 코드를 한 줄씩 해석하며 실행 (Python)
```c
int main() {
    printf("Hello, World!");
    return 0;
}
```

## 기계어
- CPU가 직접 실행할 수 있는 명령어 집합
- 각 명령어는 이진수(0, 1)로 표현되며, CPU의 명령어 세트에 따라 다름
```binary
B8 04 00 00 00 BB 01 00 00 00 B9 00 00 00 00 BA 0D 00 00 00 CD 80 B8 01 00 00 00 31 DB CD 80
```

## 어셈블리어
- 기계어와 1:1 대응되는 명령어를 사람이 이해하기 쉽게 표현
- CPU가 이해하는 기계어로 변환하기 위해 어셈블러라는 도구를 사용
```c
section .data
hello db 'Hello, World!', 0

section .text
global _start
_start:
    ; write our string to stdout
    mov eax, 4              ; system call number (sys_write)   
    mov ebx, 1              ; file descriptor (stdout)
    mov ecx, hello          ; pointer to message
    mov edx, 13             ; message length
    int 0x80                ; call kernel

    ; exit the program
    mov eax, 1              ; system call number (sys_exit)
    xor ebx, ebx            ; exit code 0
    int 0x80                ; call kernel
```

# X86 아키텍처?

## X86 아키텍처란 무엇인가?
- X86 아키텍처는 intel의 8086 CPU로 시작된 컴퓨터 프로세서 아키텍처의 한 종류
- 32bit, 64bit 버전이 있으며, 32bit 버전은 x86, 64비트 버전은 x86_64 또는 AMD64로 불림
    ### X86 아키텍처에서 32bit와 64bit의 차이는?
    - 32bit 
        - 아키텍처 : 최대 4GB의 메모리를 주소 지정할 수 있음 (2^32개의 주소)
        - 레지스터 : 레지스터 크기는 32bit (EAX, EBX, ECX, EDX)
        - 한 번에 32bit 데이터 단위를 처리
        - 함수 인수는 주로 스택을 통해 전달되며, 반환 값은 EAX 레지스터를 통해 반환
    - 64bit 
        - 아키텍처 : 최대 16EB의 메모리를 주소 지정 (2^64)
        - 레지스터 : 레지스터 크기는 64bit (RAX, RBX, RCX, RDX)
        - 한 번에 64bit 데이터 단위를 처리
        - 함수 인자는 주로 레지스터를 통해 전달되며, 반환 값은 RAX 레지스터를 통해 반환

## X86 아키텍처 주요 특징
- CISC (Complex Instruction Set Computing): 명령어가 다양하고 복잡한 연산을 수행
- 레지스터, 메모리, I/O 장치 등을 포함한 포괄적인 하드웨어 제공

## 레지스터
- 레지스터는 CPU 내부에서 데이터를 저장하고 조작하기 위한 매우 빠른 메모리 공간
- CPU는 주 메모리(RAM)보다 훨씬 빠른 속도로 레지스터에 접근할 수 있음

- X86 아키텍처에서 사용되는 주요 레지스터
    ### 일반 목적 레지스터 (32bit)
    - EAX (Accumulator): 주로 산술 연산과 데이터 이동에 사용
    - EBX (Base): 베이스 포인터로 사용
    - ECX (Count): 반복 연산의 카운터로 사용
    - EDX (Data): 확장된 산술 연산 및 I/O 포트 주소로 사용
    - ESI (Source Index): 데이터 복사 시 소스 주소로 사용
    - EDI (Destination Index): 데이터 복사 시 목적지 주소로 사용
    - EBP (Base Pointer): 스택 프레임의 베이스 포인터로 사용
    - ESP (Stack Pointer): 스택 포인터로 사용

    ### 세그먼트 레지스터
    - CS (Code Segment): 실행 중인 코드의 세그먼트 시작 주소를 저장
    - DS (Data Segment): 데이터 세그먼트의 시작 주소를 저장
    - SS (Stack Segment): 스택 세그먼트의 시작 주소를 저장
    - ES, FS, GS: 추가 데이터 세그먼트 레지스터

    ### 플래그 레지스터 (EFLAGS)
    - 조건부 연산의 결과를 저장하며, 제어 흐름 결정에 사용
    - Zero Flag (ZF)
    - Sing Flag (SF)
    - Overflow Flag (OF)
    - Carry Flag (CF)
    - Parity Flag (PF)

## 메모리 모델
- X86 아키텍처는 세그먼트와 오프셋을 사용하여 메모리를 주소 지정
- 세그먼트는 메모리의 특정 블록을 나타내고, 오프셋은 그 블록 내의 위치를 나타냄

---

# 명령어

## 데이터 이동 명령어 
- mov : 
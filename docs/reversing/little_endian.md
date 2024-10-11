---
layout: default
title: Little Endian
nav_order: 2
category: "basic"
parent: reversing
---

# 리틀 엔디언 표기법
컴퓨터에서 메모리에 데이터를 저장하는 방식을 의미하는 바이트 오더링(Byte Ordering)의 리틀 엔디언 표기법과 빅 엔디언 표기법에 대해 실습
{: .fs-6 .fw-300 }

---

## 실습 목표
- 총 4개의 (크기가 다른) 자료이 엔디언 방식에 따라서 같은 데이터를 각각 어떤 식으로 저장하는지 비교

---

## 3.1 바이트 오더링
- 바이트 오더링은 컴퓨터 메모리에서 데이터를 저장하고 읽는 방식에 대한 개념
- 바이트 오더링 방식에는 크게 두 가지가 존재 (빅 엔디언(Big Endian), 리틀 엔디언(Little Endian))
- 엔디언(Endian)은 **바이트 오더(Byte Ordering)**을 의미

{: .note-title }
> **빅 엔디언(Big Endian)**은 가장 큰 바이트가 먼저 오는 방식이다. 즉 데이터의 최상위 바이트(Most Significant Byte, NSB)가 가장 작은 메모리 주소에 저장
> **리틀 엔디언(Little Endian)**은 가장 작은 바이트가 먼저 오는 방식이다. 즉, 데이터의 최하위(Least Significant Byte, LSB)가 가장 작은 메모리 주소에 저장

## 3.2 빅 엔디언과 리틀 엔디언의 차이점
- 총 4개의 (크기가 다른) 자료형이 존재
- ![](../../assets/images/reversing/LittleEndian/1.png)

<br>

- 각 엔디언 방식에 따라서 같은 데이터를 각각 어떤 식으로 저장하는지 아래 표로 비교

| TYPE       | NAME  | SIZE  | Big Endian Style                    | Little Endian Style                 |
|------------|-------|-------|-------------------------------------|-------------------------------------|
| BYTE       | b     | 1     | [12]                                | [12]                                |
| WORD       | w     | 2     | [12][34]                            | [34][12]                            |
| DWORD      | dw    | 4     | [12][34][56][78]                    | [78][56][34][12]                    |
| char []    | str   | 6     | [61][62][63][64][65][00]            | [61][62][63][64][65][00]            |

{: .note-title }
> ASCII 문자열 마지막은 NULL로 끝이 남

<br>

- 

---


> [OllyDbg](https://www.ollydbg.de/)



---
layout: default
title: complexity
category: "etc"
nav_order: 1
parent: algorithm
---

# Complexity
{: .no_toc }

1. TOC
{:toc}

--- 

## Complexity 정의
복잡도는 알고리즘의 효율성을 평가하는 중요한 개념으로, 크게 **시간 복잡도**와 **공간 복잡도**로 나뉜다. 복잡도는 알고리즘이 실행되는 동안 얼마나 많은 시간과 메모리가 필요한지를 평가하는 척도이다.

## Time Complexity
시간 복잡도는 **알고리즘이 실행되는 데 걸리는 시간**을 입력 크기에 따라 표현한 것이다. 즉, 입력 크기(n)가 증가할 때, 알고리즘이 실행되는 시간이 얼마나 늘어나는지를 나타낸다.

## Time Complexity Big-O 표기법
시간 복잡도는 주로 Big-O 표기법으로 나타낸다. Big-O는 알고리즘이 최악의 경우 얼마나 많은 시간이 소요되는지를 나타내는 방식이다.

- O(1) : 상수 시간, 입력 크기에 상관없이 일정한 시간이 소요된다.
- O(log n) : 로그 시간, 입력 크기가 커질수록 시간 증가가 느리다.
- O(n) : 선형 시간, 입력 크기에 비례하여 시간이 증가한다.
- O(n log n) : 입력 크기가 커질수록 선형 시간보다 조금 더 빠르게 증가한다.
- O(n^2) : 이차 시간, 입력 크기가 커질수록 시간이 빠르게 증가한다.
- O(2^n) : 지수 시간, 입력 크기가 증가할 때 시간이 급격히 증가한다.

## Time Complexity 예시
- 배열의 모든 요소를 한번씩 출력하는 함수
- 이 함수는 배열의 크기(n)에 따라 요소를 순회하므로 시간 복잡도는 `O(n)`이다.

```py
def print_elements(arr):
    for element in arr:
        print(element)
```

<br>

- 버블 정렬
- 두 중첩된 반복문이 각각 배열을 순회하므로 시간 복잡도는 `O(n^2)`이다.

```py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

## Space Complexity
공간 복잡도는 알고리즘이 실행될 때 사용하는 메모리의 양을 입력 크기에 따라 표현한 것이다. 즉, **알고리즘이 실행되면서 사용하는 메모리의 양이 얼마나 증가하는지**를 나타낸다.

## Space Complexity Big-O 표기법
공간 복잡도 역시 Big-O 표기법으로 나타내며, 알고리즘이 필요로 하는 추가적인 메모리를 평가한다.




---
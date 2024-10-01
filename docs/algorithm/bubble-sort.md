---
layout: default
title: bubble sort
category: "sort"
nav_order: 2
parent: algorithm
---

# Bubble Sort
{: .no_toc }

1. TOC
{:toc}

--- 

## Bubble Sort 정의
- 버블 정렬은 인접한 두 요소를 비교하면서 작은 값이 앞에 오도록 교환하는 방식의 정렬 알고리즘이다.
- 이 과정을 배열의 끝까지 반복하면 가장 큰 값이 맨 뒤로 '거품처럼' 밀려 올라가게 된다.
- 이런 과정을 전체 배열에 대해 여러 번 반복하여 배열이 정렬된다.

## Bubble Sort 복잡도
- 시간 복잡도 : 평균 및 최악의 경우 모두 O(n^2)
- 공간 복잡도 : O(1) (추가적인 메모리를 거의 사용하지 않음)
- 작은 데이터 세트에 대해서는 쉽게 구현하고 이해할 수 있지만, 큰 데이터 세트에는 비효율적이다.

{: .no_toc}
> 


---
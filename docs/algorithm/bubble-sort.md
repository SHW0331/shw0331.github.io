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

## Bubble Sort 예시
- 배열의 첫 번째 요소와 두 번째 요소를 비교한다.
- 두 번째 요소가 더 작으면 두 요소의 위치를 교환한다.
- 두 번째 요소와 세 번째 요소를 비교하여, 더 작은 요소가 앞에 오도록 교환한다.
- 배열의 끝까지 이 과정을 반복하여 가장 큰 요소가 마지막에 오게 한다.
- 배열이 정렬될 때 까지 이 과정을 반복한다.

```py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 마지막 i개 요소는 이미 정렬되어 있으므로 비교할 필요가 없음
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 요소 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## Bubble Sort 예제
- 문제 : 주어진 숫자 배열을 **버블 정렬**을 사용해 오름차순으로 정렬하시오.
- 입력 : [5, 2, 9, 1, 5, 6]
- 출력 : [1, 2, 5, 5, 6, 9]
- 초기 접근 방식(작성자) :

```py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

input_data = [5, 2, 9, 1, 5, 6]
result = bubble_sort(input_data)
print(result) # [1, 2, 5, 5, 6, 9]
```

<br>

- 권장 접근 방식 :

```py
def bubble_sort(arr):
    n = len(arr)
    # 배열의 요소 개수만큼 반복
    for i in range(n):
        # 마지막 i개의 요소는 이미 정렬되었으므로 그 전까지만 비교
        for j in range(0, n - i - 1):
            # 인접한 두 요소를 비교하여, 앞의 요소가 더 크면 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [5, 2, 9, 1, 5, 6]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # 결과: [1, 2, 5, 5, 6, 9]
```

{: no_toc}
> **range(start, stop)**에서 **start**는 시작 인덱스를 의미하고, **stop**은 끝나는 인덱스를 의미합니다.
> **range(0, n - i - 1)**에서 **start**를 명시적으로 **0**으로 설정했지만, **range(n - i - 1)**은 암묵적으로 0부터 시작하게 되어 있습니다.
> 즉, **range(n - i - 1)**는 **range(0, n - i - 1)**와 동일하게 0부터 시작해서 n - i - 1 이전까지 순회합니다.

---
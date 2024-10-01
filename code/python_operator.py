# - 문제 : 주어진 숫자 배열을 오름차순으로 정렬하시오.
# - 입력 : [5, 2, 9, 1, 5, 6]
# - 출력 : [1, 2, 5, 5, 6, 9]

## Bubble Sort 예시
# - 배열의 첫 번째 요소와 두 번째 요소를 비교한다.
# - 두 번째 요소가 더 작으면 두 요소의 위치를 교환한다.
# - 두 번째 요소와 세 번째 요소를 비교하여, 더 작은 요소가 앞에 오도록 교환한다.
# - 배열의 끝까지 이 과정을 반복하여 가장 큰 요소가 마지막에 오게 한다.
# - 배열이 정렬될 때 까지 이 과정을 반복한다.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # i == arr[0]
        for j in range(n - i - 1): # arr[0]을 제외한 arr[1],arr[2].arr[3].arr[4], arr[5] 까지 비교
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

input_data = [5, 2, 9, 1, 5, 6]
result = bubble_sort(input_data)
print(result)

# 첫번째 2번째 비교,
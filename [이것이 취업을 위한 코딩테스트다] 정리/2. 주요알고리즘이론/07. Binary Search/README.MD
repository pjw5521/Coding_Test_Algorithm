# 07. 이진탐색

## 순차탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

## **이진탐색**
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교 
    ```python
    # 재귀함수로 구현한 이진 탐색 소스코드
    def binary_search(array, target, start ,end):
    if start > end:
        return None
    mid = ( start + end ) // 2 
    if array[mid] == target:
        return mid 
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
    ```
    ```python
    # 반복문으로 구현한 이진 탐색 소스코드
    def binary_search(array, target, start ,end):
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
            return mid 
            elif array[mid] < target:
            start = mid + 1 
            else: 
            end = mid - 1 
        return None
    ```
- 시간복잡도 : O(logN)
- 탐색 범위가 큰 상황에서 사용

## 트리자료구조
- 큰 데이터를 처리하는 소프트웨어에서 사용
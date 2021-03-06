# Two Pointers (투포인터)

## 투포인터란 ?
- 1차원 배열에서 두 개의 포인터를 조작하여 원하는 결과를 얻는 알고리즘
- 시작점과 끝점으로 접근할 데이터의 범위 표현 
- 기존 방식보다 효율성 개선 가능 
- 시간 복잡도 : O(n)

## 접근법
- 완전 탐색 문제에서 시간 초과가 발생할 때 
    - 투포인터, 이분 탐색, 그리디, dp 로 접근 가능 
    
    
# Backtracking (백트래킹)

## 백트래킹 이란 ?
- DFS를 사용하여 조건에 맞지 않으면 즉시 중단하고, 이전으로 돌아가며 다시 확인하는 것을 반복하면서 원하는 조건을 찾는 알고리즘
- 모든 경우의 수를 전부 고려하는 알고리즘 상태공간을 트리로 나타낼 수 있을 때 적합한 방식
- 일종의 트리 탐색 알고리즘 

## 알고리즘
- 기본적으로 모든 경우의 수를 탐색한다는 완전탐색(브루트 포스)전략을 취하지만, 처리 속도를 향상시키기 위해 **가지치기**가 중요한 역할
- 가지치기를 잘할수록 불필요한 경우가 제거되어 처리 속도 향상 
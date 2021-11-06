# 09. Dijkstra's

## 1. 최단 경로란 ?
- 말 그대로 가장 짧은 경로는 찾는 알고리즘

## 2. 다익스트라 최단 경로 알고리즘 
- 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘 
- 기본적으로 [그리디 알고리즘](https://github.com/pjw5521/Coding_Test_Algorithm/tree/main/%5B%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%B7%A8%EC%97%85%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4%5D%20%EC%A0%95%EB%A6%AC/2.%20%EC%A3%BC%EC%9A%94%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%A1%A0/Greedy)으로 분류 
- **방법 1** : 구현하기 쉽지만 느리게 동작하는 코드
    + 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인
    + 시간 복잡도 : O(V^2)
    + [간단한 다익스트라 알고리즘](https://github.com/pjw5521/Coding_Test_Algorithm/blob/main/%5B%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%B7%A8%EC%97%85%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4%5D%20%EC%A0%95%EB%A6%AC/2.%20%EC%A3%BC%EC%9A%94%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%A1%A0/Dijkstra's/9-1%20%EA%B0%84%EB%8B%A8%ED%95%9C%20%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.py)
- **방법 2** : 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드 
    + 우선순위 큐 : 우선 순위가 가장 높은 데이터를 가장 먼저 삭제 
    + 방법 1 기반으로, 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용 
    + 시간 복잡도 : O(Elog(V))
    + [개선된 다익스트라 알고리즘](https://github.com/pjw5521/Coding_Test_Algorithm/blob/main/%5B%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%B7%A8%EC%97%85%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4%5D%20%EC%A0%95%EB%A6%AC/2.%20%EC%A3%BC%EC%9A%94%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%A1%A0/Dijkstra's/9-2%20%EA%B0%9C%EC%84%A0%EB%90%9C%20%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.py)

## 3. 플로이드 워셜 알고리즘 
- **모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우**에 사용할 수 있는 알고리즘 
- 시간 복잡도 : O(N^3)
- 점화식 : D(a,b) = min(D(a,b) , D(a,k) + D(k,b))
- 3중 반복문 이용 
- [플로이드 워셜 알고리즘](https://github.com/pjw5521/Coding_Test_Algorithm/blob/main/%5B%EC%9D%B4%EA%B2%83%EC%9D%B4%20%EC%B7%A8%EC%97%85%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%8B%A4%5D%20%EC%A0%95%EB%A6%AC/2.%20%EC%A3%BC%EC%9A%94%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B4%EB%A1%A0/Dijkstra's/9-3%20%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C%20%EC%9B%8C%EC%85%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.py)
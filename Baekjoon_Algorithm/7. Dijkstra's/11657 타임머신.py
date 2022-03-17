# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline 

def bf(start):
  distance[start] = 0
  # 정점 수만큼 반복 
  for i in range(n):
    # 모든 간선 확인 
    for j in range(m):
      # 현재 노드 
      node = edges[j][0]
      # 다음 노드 
      next_node = edges[j][1]
      # 가중치 
      cost = edges[j][2]

      # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧으면
      if distance[node] != INF and distance[next_node] > distance[node] + cost:
        # 갱신 
        distance[next_node] = distance[node] + cost
        # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재한다는 것이므로 
        if i == n-1:
          return True

  return False

n, m = map(int,input().split())

edges = []
INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int,input().split())
  edges.append((a,b,c))

cycle = bf(1)

if cycle:
  print(-1)
else:
  for i in range(2,n+1):
    if distance[i] == INF:
      print(-1)
    else:
      print(distance[i])
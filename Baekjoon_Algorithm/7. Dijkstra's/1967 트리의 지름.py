# https://www.acmicpc.net/problem/1967
import heapq

INF = int(1e9)
def dijkstra(start):
  distance = [INF] * (n+1)
  distance[start] = 0

  q = []
  heapq.heappush(q,(0,start))

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance
  
n = int(input())

INF = int(1e9)
graph = [ [] for _ in range(n+1) ]

for _ in range(n-1):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

# 1번 노드에서 다른 노드까지의 거리 구하기
distance = dijkstra(1)
# 다른 노드까지의 거리 중 가장 긴 것의 노드 번호 구하기 
tmp = distance.index(max(distance[1:]))
# 구한 노드 번호에서 다른 노드까지의 거리 중 가장 긴 것 출력 
print(max(dijkstra(tmp)[1:]))
# https://www.acmicpc.net/problem/1504
# 양방향 경로임 
import sys
input = sys.stdin.readline
import heapq

n, e = map(int,input().split())

INF = int(1e9)

graph = [ [] for _ in range(n+1) ]

for _ in range(e):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

v1, v2 = map(int,input().split())

def dijkstra(start, end):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0
  while q :
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기 
    dist, now = heapq.heappop(q)
    # 이미 처리된 적이 있으면 무시 
    if distance[now] < dist :
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))
  
  return distance[end]

result1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2,n)
result2 =  dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1,n)

if result1 >= INF and result2 >= INF:
  print(-1)
else:
  print(min(result1, result2))
# https://www.acmicpc.net/problem/1238
import sys, heapq 
input = sys.stdin.readline 

def dijkstra(start):
  distance = [INF] * (n+1)
  distance[start] = 0 
  q = []
  heapq.heappush(q,(0,start))

  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        heapq.heappush(q,(cost,i[0]))
        distance[i[0]] = cost 

  return distance
        
n, m, x = map(int,input().split())

INF = int(1e9)
graph = [ [] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))

# x에서 다른 노드까지의 거리 저장
dist = dijkstra(x)
result = 0 
for i in range(1,n+1):
  # i에서 다른 노드까지의 거리 
  tmp = dijkstra(i)
  # i에서 x 까지의 최단 거리 + x에서 i까지 최단 거리 최솟값 구하기 
  result = max(result, dist[i] + tmp[x])

print(result)
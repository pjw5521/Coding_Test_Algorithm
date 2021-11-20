# https://www.acmicpc.net/problem/14496
import sys
input = sys.stdin.readline
import heapq
a,b = map(int,input().split())
n, m = map(int,input().split())
INF = int(1e9)
graph = [ [] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  c, d = map(int,input().split())
  graph[c].append((d,1))
  # 양방향으로 해줘야함 
  graph[d].append((c,1)) 

def dijkstra(start):
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

dijkstra(a)

if distance[b] == INF:
  print("-1")
else : print(distance[b])
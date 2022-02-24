# https://www.acmicpc.net/problem/1753
import sys
import heapq
input = sys.stdin.readline 
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0,start))
  # 시작 정점의 가중치 0 으로 
  distance[start] = 0
  while q :
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기 
    dist, now = heapq.heappop(q)
    # 이미 처리된 적이 있으면 무시 
    if distance[now] < dist :
      continue
    for w, node in graph[now]:
      cost = dist + w
      if cost < distance[node]:
        distance[node] = cost
        heapq.heappush(q,(cost,node))
        
v, e = map(int,input().split())

start = int(input())

graph = [ [] for i in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
  a, b, c = map(int,input().split())
  # (가중치, 목적지 노드)
  graph[a].append((c,b))
  
dijkstra(start)

for i in range(1, v+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
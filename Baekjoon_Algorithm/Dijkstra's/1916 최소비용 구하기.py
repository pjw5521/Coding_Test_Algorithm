#https://www.acmicpc.net/problem/1916
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [ [] for _ in range(n+1) ]
distance = [INF] * (n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

start, end = map(int,input().split())

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

dijkstra(start)

print(distance[end])
# https://www.acmicpc.net/problem/10282
import heapq
import sys
input = sys.stdin.readline

test_num = int(input())

def dijkstra(graph, start):
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
  cnt = 0
  result = 0
  for i in distance:
    if i != INF:
      cnt += 1
      result = max(result,i)
  print(cnt, result)

for _ in range(test_num):
  n, d, c = map(int,input().split())
  
  INF = int(1e9)

  graph = [ [] for _ in range(n+1) ]
  
  for _ in range(d):
    a, b, s = map(int,input().split())
    graph[b].append((a,s))

  dijkstra(graph, c)
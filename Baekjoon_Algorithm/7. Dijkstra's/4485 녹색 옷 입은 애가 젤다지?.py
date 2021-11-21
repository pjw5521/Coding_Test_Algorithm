# https://www.acmicpc.net/problem/4485
import sys
input = sys.stdin.readline
import heapq

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]
INF = int(1e9)

def dijkstra():
  q = []
  heapq.heappush(q, (graph[0][0],0,0))
  distance[0][0] = 0
  while q :
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기 
    cost, x, y = heapq.heappop(q)
    # 이미 처리된 적이 있으면 무시 
    if x == n-1 and y == n-1:
      print(f'Problem {cnt}: {distance[n-1][n-1]}')
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if ( 0<= nx < n) and ( 0<= ny < n):
        new_cost = cost + graph[nx][ny]
        if new_cost < distance[nx][ny]:
          distance[nx][ny] = new_cost
          heapq.heappush(q, (new_cost,nx,ny))

cnt = 1
while True:
  n = int(input())
  
  if n == 0:
    break

  graph = []
  distance = [ [INF] * (n) for _ in range(n) ]

  for _ in range(n):
    graph.append(list(map(int,input().split())))

  dijkstra()
  cnt += 1 
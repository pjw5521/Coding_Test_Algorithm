# bfs로 품 
# https://www.acmicpc.net/problem/1261

from collections import deque

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]
INF = int(1e9)

m, n  = map(int,input().split())

distance = [ [-1] *m for _ in range(n) ]

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

queue = deque()
queue.append((0,0))
distance[0][0] = 0 
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if ( 0 <= nx < n ) and ( 0 <= ny < m
    ):
      if distance[nx][ny] == -1:
        if graph[nx][ny] ==0:
          distance[nx][ny] = distance[x][y]
          # 흰방이면 앞에 추가
          queue.appendleft((nx,ny))
        else:
          distance[nx][ny] = distance[x][y] + 1
          queue.append((nx,ny))

print(distance[n-1][m-1])

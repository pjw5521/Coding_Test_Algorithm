# https://www.acmicpc.net/problem/2665
# 알고스팟과 비슷한 문제 

from collections import deque

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]
INF = int(1e9)

n  = int(input())
distance = [ [-1] *n for _ in range(n) ]

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
    if ( 0 <= nx < n ) and ( 0 <= ny < n
    ):
      if distance[nx][ny] == -1:
        if graph[nx][ny] ==1:
          distance[nx][ny] = distance[x][y]
          # 흰방이면 앞에 추가
          queue.appendleft((nx,ny))
        else:
          distance[nx][ny] = distance[x][y] + 1
          queue.append((nx,ny))

print(distance[n-1][n-1])

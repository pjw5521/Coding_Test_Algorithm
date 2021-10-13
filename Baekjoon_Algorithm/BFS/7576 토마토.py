# 문제 https://www.acmicpc.net/problem/7576
# bfs로 최단거리 구하는 문제 

from collections import deque

n, m = map(int, input().split())
queue = deque()
graph = []
for i in range(m):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    # 토마토의 위치를 미리 queue에 저장해둬야 함 ! 
    if graph[i][j] == 1:
      queue.append((i,j))

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

def bfs(): 
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if ( 0 <= nx < m ) and ( 0 <= ny < n
      ) and graph[nx][ny] == 0:
        graph[nx][ny] = graph[a][b] + 1 
        queue.append((nx,ny))

bfs()
result =0
# 최단거리 구하기 
for i in graph:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  result = max(result, max(i))


print(result-1)
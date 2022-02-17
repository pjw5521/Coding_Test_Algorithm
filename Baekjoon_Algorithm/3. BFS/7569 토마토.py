# https://www.acmicpc.net/problem/7569
from collections import deque 
import sys
input = sys.stdin.readline 

dh = [ 1, -1 , 0, 0 , 0, 0 ]
dx = [ 0 ,0, 1, -1, 0, 0 ]
dy = [ 0, 0, 0, 0, 1, -1 ]

def bfs():
  
  while q:
    x, y, z = q.popleft()
    
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 대하여 탐색 
    for i in range(6):
      nh = x + dh[i]
      nx = y + dx[i]
      ny = z + dy[i]
      if 0<= nh < h and  0 <= nx < n and 0 <= ny < m and graph[nh][nx][ny] == 0:
        graph[nh][nx][ny] = graph[x][y][z] + 1 
        q.append((nh, nx,ny))

m, n, h = map(int,input().split())

graph = []
  
for i in range(h):
  tmp = []
  for j in range(n):
    tmp.append(list(map(int,input().split())))
  graph.append(tmp)
  
q = deque()

# 토마토 위치 저장 
for k in range(h):
  for i in range(n):
    for j in range(m):
      if graph[k][i][j] == 1:
        q.append((k,i,j))

bfs()
result = 0

for k in graph:
  for i in k:
    for j in i:
      if j == 0:
        print(-1)
        exit(0)
      result = max(result, j)

print(result-1)
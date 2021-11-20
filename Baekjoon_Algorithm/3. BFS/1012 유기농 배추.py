#https://www.acmicpc.net/problem/1012
from collections import deque
test_num = int(input())

dx = [ -1 ,0, 1, 0 ]
dy = [ 0, -1, 0, 1 ]

def bfs(x,y):
  q = deque()
  q.append((x,y))
  while q :
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if ( 0<= nx <n )and (0<=ny <m) and graph[nx][ny] == 1 :
        graph[nx][ny]= 0 
        q.append((nx,ny))

for _ in range(test_num):
  m,n,k = map(int,input().split())

  graph = [ [0]* m for _ in range(n)]

  for _ in range(k):
    a,b = map(int,input().split())
    graph[b][a] = 1

  count = 0 
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1 :
        bfs(i,j)
        count += 1 

  print(count)
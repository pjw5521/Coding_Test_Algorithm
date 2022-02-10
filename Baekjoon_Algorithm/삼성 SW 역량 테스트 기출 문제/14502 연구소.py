# https://www.acmicpc.net/problem/14502
# pypy3로 하면 시간초과 안나지만 python3으로 하면 시간 초과 
# bfs 문제 
from collections import deque 
import copy
import sys

input = sys.stdin.readline

dx = [ -1 , 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

q = deque()

def bfs():
  global answer 
  graph = copy.deepcopy(maps)

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2 :
         q.append((i,j))

  while q :
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 0 :
        graph[nx][ny] = 2
        q.append((nx,ny))
  
  cnt = 0
  # 0인 곳 개수 구함 
  for i in graph:
    cnt += i.count(0)

  answer = max(answer, cnt)

def wall(x):
  if x == 3 :
    bfs()
    return 

  for i in range(n):
    for j in range(m):
      if maps[i][j] == 0:
        maps[i][j] = 1 
        wall(x+1)
        maps[i][j] = 0 

n, m = map(int,input().split())

maps = []
answer = 0 

for _ in range(n):
  maps.append(list(map(int,input().split())))

wall(0)

print(answer)

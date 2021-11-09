# 문제 344쪽 
# https://www.acmicpc.net/problem/18405

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

# 바이러스 지도
graph = []
# 바이러스 정보 저장 
data = [] 

dx = [ -1, 0, 1, 0 ]
dy = [ 0, -1, 0, 1 ]

for i in range(n):
  graph.append(list(map(int,input().split())))
  # 바이러스가 있는 곳 위치 저장 
  for j in range(n):
    if graph[i][j] != 0 :
      data.append((graph[i][j], 0, i, j))

# 낮은 순으로 
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int,input().split())

# bfs
while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0<= ny < n and graph[nx][ny] == 0:
      q.append((virus,s+1,nx,ny))
      graph[nx][ny] = virus

print(graph[target_x-1][target_y-1])

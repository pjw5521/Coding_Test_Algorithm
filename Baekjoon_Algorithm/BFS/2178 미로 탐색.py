# 문제 https://www.acmicpc.net/problem/2178
# 최단거리 문제 
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):

  q = deque()
  q.append((x, y))

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if ( 0 <= nx < n ) and ( 0 <= ny < m) and graph[nx][ny] == 1:
        q.append((nx,ny))
        graph[nx][ny] = graph[x][y] +1
    # n-1, m-1 위치까지의 거리
  return graph[n-1][m-1]

print(bfs(0, 0))
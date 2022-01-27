# https://www.acmicpc.net/problem/2206
from collections import deque 

nx = [ 1, -1, 0, 0 ]
ny = [ 0, 0, 1, -1 ]

def bfs():
  
  visited = [ [[0] * 2 for _ in range(m)] for _ in range(n)]

  visited[0][0][1] = 1 
  q = deque()
  q.append((0,0,1))

  while q : 
    x, y, w = q.popleft()

    if x == n-1 and y == m-1 :
      return visited[x][y][w]

    for v in range(4):
      dx = x + nx[v]
      dy = y + ny[v]

      if 0<= dx < n and 0<= dy < m:
        if maps[dx][dy] == 0 and visited[dx][dy][w] == 0:
          visited[dx][dy][w] = visited[x][y][w] + 1 
          q.append((dx,dy,w))
        elif maps[dx][dy] == 1 and w == 1 :
          visited[dx][dy][0] = visited[x][y][1] + 1 
          q.append((dx, dy, 0))

  return -1

n, m = map(int,input().split())

maps = []

for _ in range(n):
  maps.append(list(map(int,input())))

print(bfs())
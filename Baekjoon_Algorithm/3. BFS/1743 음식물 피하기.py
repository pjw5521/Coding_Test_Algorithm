#https://www.acmicpc.net/problem/1743
from collections import deque 

nx = [ 1, -1, 0 , 0 ]
ny = [ 0, 0, 1, -1 ]

def bfs(i,j):
  q = deque()
  q.append((i,j))
  count = 1 
  maps[i][j] = 0 
  while q:
    x, y = q.popleft()

    for i in range(4):
      dx = x + nx[i]
      dy = y + ny[i]
      if 0 <= dx < n and 0<= dy < m and maps[dx][dy] == 1 :
        maps[dx][dy] = 0 
        q.append((dx,dy))
        count +=1 

  return count 

n, m , k = map(int,input().split())

maps = [ [0] * m for _ in range(n)]

for _ in range(k):
  a,b = map(int,input().split())
  maps[a-1][b-1] = 1 

max_num = 0 
for i in range(n):
  for j in range(m):
    if maps[i][j] == 1 :
      tmp = bfs(i,j)
      if tmp > max_num:
        max_num = tmp

print(max_num)
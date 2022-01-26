#https://www.acmicpc.net/problem/1303
from collections import deque 

nx = [ 1, -1, 0, 0 ]
ny = [ 0, 0, 1, -1 ]

def bfs(color,i,j):
  # 병사 수 
  count = 1 
  
  q= deque()
  q.append((i,j))
  # 방문 표시 
  maps[i][j] = "#"
  
  while q :
    x, y = q.popleft()

    for i in range(4):
      dx = x + nx[i]
      dy = y + ny[i]
    
      if 0 <= dx < m and 0 <= dy < n and maps[dx][dy] == color:
        count += 1
        maps[dx][dy] = "#"
        q.append((dx,dy))

  return count

n, m = map(int,input().split())

maps = []

for _ in range(m):
  maps.append(list(map(str,input())))

b_num = 0
w_num = 0 

for i in range(m):
  for j in range(n):
  
    if maps[i][j] == 'B':
      tmp = bfs('B',i,j)
      b_num += tmp * tmp 
      
    elif maps[i][j] == 'W':
      tmp = bfs('W',i,j)
      w_num += tmp * tmp 

print(w_num,b_num)
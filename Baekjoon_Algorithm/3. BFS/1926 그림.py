from collections import deque 

nx = [ 1, -1, 0, 0 ]
ny = [ 0, 0, 1, -1 ]

def bfs(x,y):
  q= deque()
  q.append((x,y))
  num = 1 
  maps[x][y] = 0
  while q :
    x, y = q.popleft()
    for i in range(4):
      dx = x + nx[i]
      dy = y + ny[i]

      if 0 <= dx < n and 0<= dy < m and maps[dx][dy] == 1 :
        maps[dx][dy] = 0
        num += 1 
        q.append((dx,dy))
  
  return num 

n, m = map(int,input().split())

maps = []

for _ in range(n):
  maps.append(list(map(int,input().split())))

# 그림 개수 저장 
count = 0
# 그림 넓이 저장할 배열 
result = []
for i in range(n):
  for j in range(m):
    if maps[i][j] == 1:
      count += 1 
      result.append(bfs(i,j))

print(count)

if result :
  print(max(result))
else:
  print(0)
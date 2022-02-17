# https://www.acmicpc.net/problem/10026
from collections import deque 

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

# 적록색약이 아닌 사람 
def bfs(a,b):
  visited[a][b] = 1

  q = deque()
  q.append((a,b))
  
  # 어떤 색인지 
  start = graph[a][b]
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위에 포함되고 색이 같고 방문하지 않았으면 
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == start and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx,ny))

  return 1 

# 적록색약인 사람의 R, G 경우
def bfs_another(a,b):
  visited[a][b] = 1

  q = deque()
  q.append((a,b))
  
  start = graph[a][b]
  
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # R 또는 G 일 때 모두 이동 가능 
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in ('G', 'R') and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        q.append((nx,ny))
  
  return 1 
  
n = int(input())

graph = []

for _ in range(n):
  graph.append(list(input()))

visited = [ [0] * n for _ in range(n) ]

answer = [0] * 2
for i in range(n):
  for j in range(n) :
    if visited[i][j] == 0:
      answer[0] += bfs(i,j)

visited = [ [0] * n for _ in range(n) ]

for i in range(n):
  for j in range(n) :
    if visited[i][j] == 0:
      if graph[i][j] in ('R','G'):
      	answer[1] += bfs_another(i,j)
      else:
       	answer[1] += bfs(i,j)
      	
print(*answer)
# https://www.acmicpc.net/problem/3190
# bfs 문제 
from collections import deque 

# 오른쪽 아래쪽 왼쪽 위쪽 
dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0]

def bfs():
  x, y = 1, 1 
  # 뱀이 있는 곳 2로 표현  
  graph[x][y] = 2
  # 방향 
  direction = 0 
  # 뱀의 몸 
  q = deque()
  q.append((x,y))
  
  # 시간 
  t = 0
  # 이동 경로 인덱스 
  index = 0 

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 범위에 있고 뱀의 몸이 아니면 
    if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 2 :
      # 사과가 아니면 
      if graph[nx][ny] == 0 :
        # 뱀이 한칸 앞으로 이동 
        graph[nx][ny] = 2
        q.append((nx,ny))
        # 뱀의 몸 길이 줄이기 
        px, py = q.popleft()
        graph[px][py] = 0
      # 사과면 
      if graph[nx][ny] == 1 :
        # 뱀이 한칸 앞으로 이동 
        graph[nx][ny] = 2
        q.append((nx,ny))
    else :
      t += 1
      break
    
    x = nx
    y = ny 
    t += 1
    if index <len(data) and t == data[index][0]:
      direction = turn(direction, data[index][1])
      index += 1 

  return t

# 회전 
def turn(direction, c):
  if c == 'L':
    direction = (direction -1)%4
  else:
    direction = (direction +1)%4

  return direction 

# 보드의 크기 
n = int(input())

# 사과의 개수
k = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
  a, b = map(int,input().split())
  graph[a][b] = 1

data = []
# 뱀의 방향 변환 횟수 
l = int(input())

for _ in range(l):
  x, c = input().split()
  data.append((int(x), c))

print(bfs())
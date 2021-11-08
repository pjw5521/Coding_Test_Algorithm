# 문제 327쪽 
# https://www.acmicpc.net/problem/3190

# 보드의 크기 
n = int(input())
graph = [ [0] * (n+1) for _ in range(n+1) ]

# 사과의 개수
k = int(input())
# 사과 위치 표시
for _ in range(k):
  a,b = map(int,input().split())
  graph[a][b] = 1 

# 회전 개수
L = int(input())
# 회전 정보 기록 
info = []
for _ in range(L):
  x, c = input().split()
  info.append((int(x),c))

# 동남서북 ( 처음에 오른쪽(동쪽) 보고 있음 )  
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 회전 
def turn(direction, c):
  if c == 'L':
    direction = (direction -1)%4
  else:
    direction = (direction +1)%4
  return direction 

def simulate():
  x,y = 1, 1 # 머리 위치
  # 존재하는 곳 2로 표시 
  graph[x][y] = 2
  direction = 0
  # 위치 정보 표시 
  q = [ (x,y) ]
  time = 0 
  index = 0 
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 벽이 아니고 뱀이 존재하지 않음 
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and graph[nx][ny] != 2 :
      # 사과가 없을 때, 머리 앞으로 이동 꼬리도 앞으로 이동 
      if graph[nx][ny] == 0 :
        graph[nx][ny] = 2 
        q.append((nx,ny))
        px, py = q.pop(0)
        graph[px][py] = 0
    # 사과가 있을 때 머리만 앞으로 이동 
      if graph[nx][ny] == 1:
        graph[nx][ny] = 2 
        q.append((nx,ny))
    # 벽에 부딪혔을 때 
    else:
      time += 1
      break
    x = nx
    y = ny 
    time += 1 
    # 회전해야될 때 
    if index < len(info) and time == info[index][0] :
      direction = turn(direction,info[index][1])
      index += 1 

  return time

print(simulate())





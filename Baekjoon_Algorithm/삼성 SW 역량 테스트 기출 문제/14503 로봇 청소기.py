# https://www.acmicpc.net/problem/14503
# 그래프 문제 
dx = [ -1, 0, 1, 0 ]
dy = [ 0, 1, 0, -1 ]

def turn():
  global d 
  d = (d-1) % 4 

n, m = map(int,input().split())
x, y, d = map(int,input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int,input().split())))

# 출발 지점 방문 표시 
graph[x][y] = 2
count = 1 

while True :
  # 네 방향에 청소할 공간이 있는지 확인 
  check = False 
  # 왼쪽으로 회전 
  for _ in range(4):
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0<= ny < m :
      # 청소할 공간이 있다면 
      if graph[nx][ny] == 0 :
        count += 1 
        # 방문 표시 
        graph[nx][ny] = 2
        # 청소할 공간이 있음을 표시 
        check = True 
        # 이동 
        x, y = nx, ny 
        break 
  # 청소할 공간이 없다면 
  if not check :
    # 후진 
    nx = x - dx[d]
    ny = y - dy[d]
    if 0<= nx < n and 0<= ny < m :
      # 후진 
      if graph[nx][ny] == 2 :
        x, y = nx, ny
      # 벽이라 후진할 수 없다면 
      if graph[nx][ny] == 1 :
        print(count)
        break
    # 후진할 수 없다면 
    else :
      print(count)
      break

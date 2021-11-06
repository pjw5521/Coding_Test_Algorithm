# n은 세로 길이, m은 가로 길이
n, m = map(int, input().split(" "))
# 방문했는지를 표시하기 위함 
d = [ [0] * m for _ in range(n)]
# x, y는 현재 좌표,  direction는 현재 방향
x, y, direction = map(int, input().split(" "))
# 방향에 따른 x,y 이동방향 
dirx = [ -1, 0 , 1 , 0 ]
diry = [ 0, 1, 0, -1 ]
# 현재 위치 방문 표시 
d[x][y] = 1
# 지도 
a = []
for i in range(n):
  a.append(list(map(int,input().split(" "))))

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dirx[direction]
  ny = y + diry[direction]
  if d[nx][ny] ==0 and a[nx][ny] == 0:
    d[nx][ny] = 1
    count += 1 
    turn_time = 0 
    x = nx
    y = ny
    continue
  else : 
    turn_time += 1
  if turn_time == 4:
    nx = x - dirx[direction]
    ny = y - diry[direction]
    if a[nx][ny] == 0:
      x = nx 
      y = ny
    else:
      break
    turn_time = 0 

print(count)
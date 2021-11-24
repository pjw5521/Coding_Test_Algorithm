# https://www.acmicpc.net/problem/2580
# 백트래킹 + dfs 
import sys
input = sys.stdin.readline

data = []
for _ in range(9):
  data.append(list(map(int,input().split())))

blank = []
for i in range(9):
  for j in range(9):
    if data[i][j] == 0:
    # 빈칸 위치 저장
      blank.append((i,j))

# 가로에 숫자 체크
def check_row(x,a):
  for i in range(9):
    if a == data[x][i]:
      return False
  return True

# 세로 숫자 체크
def check_col(y,a):
  for i in range(9):
    if a == data[i][y]:
      return False
  return True

# 3 * 3 숫자 체크 
def check_rect(x,y,a):
  nx = x//3 * 3 
  ny = y//3 * 3 
  for i in range(3):
    for j in range(3):
      if a == data[nx+i][ny+j]:
        return False
  return True

def dfs(idx):
  if idx == len(blank):
    for i in range(9):
      print(*data[i])
    exit(0)
  for i in range(1,10):
    x = blank[idx][0]
    y = blank[idx][1]

    if check_row(x,i) and check_col(y,i) and check_rect(x,y,i):
      data[x][y] = i # 유망한 숫자 중 하나 넣어줌 
      dfs(idx+1) # 다음 blank로 넘어감
      data[x][y] = 0 # 정답이 없을 경우 초기화 

dfs(0)
# https://www.acmicpc.net/problem/1074
n, r, c = map(int,input().split())

# 좌표를 몇 번째로 방문하는지 좌표에 해당하는 값 
cnt = 0

# n이 1이면 멈춤 
while n > 1:
  size = (2**n)//2
  # 제 2사분면 : 좌표 수정 x 
  if r < size and c < size:
    pass 
  # 제 1 사분면 : c 좌표 수정
  elif r < size and c >= size:
    cnt += size*size 
    c -= size 
  # 제 3 사분면 : r 좌표 수정 
  elif r >= size and c < size:
    cnt += size*size * 2. 
    r -= size 
  # 제 4사분면 : r,c 좌표 수정 
  elif r >= size and c >= size:
    cnt += size*size *3
    c -= size
    r -= size 
  n -= 1 

cnt = int(cnt)
# 제 2사분면 
if r == 0 and c == 0:
  print(cnt)
# 제 1사분면 
if r == 0 and c == 1 :
  print(cnt + 1)
# 제 3사분면 
if r == 1 and c == 0:
  print(cnt + 2)
# 제 4사분면 
if r == 1 and c== 1:
  print(cnt +3)
# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  s = input()

  n = int(input())

  data = input()
  
  # 숫자의 개수가 0이 아니면 
  if n :
    # 처음과 끝에 괄호 제거해주고 ',' 기준으로 잘라서 숫자만 넣어줌 
    q = deque(data[1:-2].split(','))
  else:
    q= deque()

  result = True 
  
  # 1은 현재 방향, 0은 거꾸로 뒤집은 방향 
  # 1인 경우 popleft(), 0인 경우 pop()
  index = 1
  
  for i in s:
    # 방향 바꿔주기
    if i == 'R':
      if index == 1 :
        index = 0 
      else:
        index = 1 
        
    # 방향에 따라 처음 숫자 제거 
    if i == 'D':
      if q:
        if index == 1 :
          q.popleft()
        else:
          q.pop()
      else:
        print('error')
        result = False
        break

  if result : 
    if index :
      print("[" + ",".join(q) + "]")
    # 방향이 바뀌었으면 reverse 해서 출력 
    else:
      q.reverse()
      print("[" + ",".join(q) + "]")
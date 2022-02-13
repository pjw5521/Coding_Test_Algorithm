# https://www.acmicpc.net/problem/11723
#비트 마스킹 사용 
import sys
input = sys.stdin.readline

n = int(input())

s = [0] * 21 
for _ in range(n):
  c = input().split()
  
  # 명령어의 길이에 따라 
  if len(c) == 1 :
    command = c[0]
  else:
    command = c[0]
    num = int(c[1])
 
  # 존재함을 표시하는 1
  if command == 'add':
    s[num] = 1 
  # 없음을 표시하는 0 
  elif command == 'remove':
    s[num] = 0
  elif command == 'check':
    if s[num] == 1 :
      print(1)
    else:
      print(0)
  elif command == 'toggle':
    if s[num] == 1 :
      s[num] = 0 
    else:
      s[num] = 1
  # 모두 존재 
  elif command == 'all':
    s = [1] * 21 
  # 공집합 
  else:
    s = [0] * 21


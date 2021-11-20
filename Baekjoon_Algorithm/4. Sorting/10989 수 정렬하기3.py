# https://www.acmicpc.net/problem/10989
# 시간 초과가 중요한 문제

# 아래 코드 사용 시 메모리 초과 
'''
import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
  data.append(int(input()))

data.sort()

for i in data:
  print(i)
'''

import sys
input = sys.stdin.readline

n = int(input())
check_data = [0] * 10001

for _ in range(n):
  num = int(input())
  check_data[num] = check_data[num] + 1

for i in range(1, 10001):
  if check_data[i] != 0:
    for _ in range(check_data[i]):
      print(i)
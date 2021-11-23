# https://www.acmicpc.net/problem/9461
import sys
input = sys.stdin.readline
result = [0] * 100
result[0] = 1
result[1] = 1
result[2] = 1

test_num = int(input())

for _ in range(test_num):
  n = int(input())

  if n == 1 or n == 2 or n == 3:
    print(1)
  
  else:
    for i in range(3, n):
      result[i] = result[i-2] + result[i-3]
    print(result[n-1])
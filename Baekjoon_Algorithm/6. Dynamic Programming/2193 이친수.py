# https://www.acmicpc.net/problem/2193
n = int(input())

if n == 1 or n == 2:
  print(1)
else:
  result = [0] * (n+1)
  result[0] = 1 
  result[1] = 1
  for i in range(2, n):
    result[i] = result[i-1] + result[i-2]

  print(result[n-1])
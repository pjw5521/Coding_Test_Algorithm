# https://www.acmicpc.net/problem/17626
import sys
input = sys.stdin.readline

n = int(input())

if n == 1 or n == 2:
  print(n)
else:
    
  INF = int(1e9)
  dp = [0] * (n+1)

  dp[1] = 1
  dp[2] = 2

  # n보다 작거나 같은 최대 제곱수 1 + n과 해당 제곱수의 차이의 dp 값 

  for i in range(3,n+1):
    
    min_value = INF
    num = 1
    # i보다 작거나 같은 최대 제곱수
    while num*num <= i:
      min_value = min(min_value, dp[i-num*num])
      num += 1 
    
    dp[i] = 1 + min_value

  print(dp[n])
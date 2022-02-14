# https://www.acmicpc.net/problem/11727
# dp[i] = 2*dp[i-2] + dp[i-1] 
import sys
input= sys.stdin.readline

n = int(input())

if n == 1:
  print(n)
elif n == 2:
  print(3)
else:
  dp = [0] * n
  
  dp[0] = 1
  dp[1] = 3

  for i in range(2,n):
    dp[i] = dp[i-1] + 2*dp[i-2]

  print(dp[n-1]%10007)
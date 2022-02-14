# https://www.acmicpc.net/problem/11659
# 누적 합 구하기
import sys
input= sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int,input().split()))

dp = [0] * (n+1)

dp[1] = num[0]

# 누적 합저장 
for i in range(2,n+1):
  dp[i] += dp[i-1] + num[i-1]

for _ in range(m):
  a, b = map(int,input().split())
  
  # 구간 합 구하기
  print(dp[b]-dp[a-1])
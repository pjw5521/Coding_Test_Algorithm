# https://www.acmicpc.net/problem/10844
n = int(input())

# dp[자리수][마지막 숫자] = 경우의 수 

dp =[ [0] * 10 for _ in range(n+1) ]

# 맨 앞에 올 수 있는 숫자들의 경우의 수 계산
for i in range(1,10):
  dp[1][i] = 1 

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] 
    dp[i][9] = dp[i-1][8]

for j in range(1,9):
  	dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%1000000000)
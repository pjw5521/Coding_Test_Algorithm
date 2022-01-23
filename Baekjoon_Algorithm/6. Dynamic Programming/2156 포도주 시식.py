#https://www.acmicpc.net/problem/2156
# 계단 오르기 문제와 유사 
n = int(input())

wine = []

for _ in range(n):
  wine.append(int(input()))

if n == 1 :
  print(wine[0])
elif n == 2 :
  print(wine[0]+wine[1])
else :

  dp = [0] * n
  dp[0] = wine[0]
  dp[1] = wine[0] + wine[1]

  dp[2] = max(wine[0]+ wine[2], dp[1], wine[1]+ wine[2])

  for i in range(3,n):
    dp[i] = max(wine[i]+dp[i-2], dp[i-1], wine[i]+wine[i-1]+dp[i-3])

  print(max(dp))
# https://www.acmicpc.net/problem/14501
n = int(input())

data = []

for _ in range(n):
  a, b = map(int,input().split())
  data.append((a,b))

# n일까지 상담했을 때 얻을 수 있는 최대의 수익 
dp = [0] * (n+1)

for i in range(n-1, -1, -1 ):
  if i + data[i][0] > n :
    dp[i] = dp[i+1]
  else :
    # 일을 할 때랑 안할 때 
    dp[i] = max(dp[i+1], data[i][1] + dp[i+data[i][0]] )

print(dp[0])
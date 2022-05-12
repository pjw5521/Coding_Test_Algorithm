# https://www.acmicpc.net/problem/2294
n, k = map(int,input().split())

coin = []

for _ in range(n):
    num = int(input())
    coin.append(num)
  
# dp[i] : i 숫자를 만들 때 필요한 최소 동전 개수 
dp = [10001] * (k+1)
# 0원은 0개 
dp[0] = 0 

for i in range(n):
    for j in range(coin[i], k+1):
        # 동전 금액만큼 빼고 해당 동전을 하나 추가했을 때와 비교 
        dp[j] = min(dp[j], dp[j-coin[i]] + 1)
    
# 만들 수 있다면
if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)
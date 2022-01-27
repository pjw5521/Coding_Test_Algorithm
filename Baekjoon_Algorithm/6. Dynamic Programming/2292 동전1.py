# https://www.acmicpc.net/problem/2293
n, k = map(int,input().split())

coins = []

# 각 인덱스에 해당하는 가격을 동전들로 만들 수 있는 경우의 수 
answer = [0] * (k+1)

answer[0] = 1 

for _ in range(n):
  coins.append(int(input()))

for coin in coins:
  for price in range(coin, k+1):
      answer[price] += answer[price-coin]

# k를 만들 수 있는 경우의 수
print(answer[k])
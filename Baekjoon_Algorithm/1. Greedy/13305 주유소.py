#https://www.acmicpc.net/problem/13305
n = int(input())

load = list(map(int,input().split()))

price = list(map(int,input().split()))

result = load[0] * price[0]
low_price = price[0]
for i in range(1,n-1):
  low_price = min(low_price, price[i])
  result += low_price * load[i]

print(result)
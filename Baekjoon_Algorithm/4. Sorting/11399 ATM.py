# 문제 https://www.acmicpc.net/problem/11399
n = int(input())

data = list(map(int,input().split()))

data.sort()

for i in range(1,n):
  data[i] += data[i-1]

print(sum(data))

# https://www.acmicpc.net/problem/2217
n = int(input())

data = []

for _ in range(n):
  data.append(int(input()))

data.sort()

answer = 0

for i in range(len(data)):
  answer = max(data[i]*(n-i), answer)
  
print(answer)
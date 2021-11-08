# 문제 359쪽
# https://www.acmicpc.net/problem/10825

n = int(input())

data = []

for _ in range(n):
  a,b,c,d = input().split()
  data.append((a, int(b), int(c), int(d)))

data.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in data:
  print(i[0])
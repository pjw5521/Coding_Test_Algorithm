
# 문제 https://www.acmicpc.net/problem/10815
n = int(input())
data = set(map(int,input().split()))

m = int(input())
search = list(map(int,input().split()))

for i in search:
  if i in data:
    print(1, end = " ")
  else:
    print(0, end = " ")
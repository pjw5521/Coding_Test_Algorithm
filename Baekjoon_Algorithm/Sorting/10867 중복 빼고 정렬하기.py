# 문제 https://www.acmicpc.net/problem/10867
n = int(input())

data = list(map(int,input().split()))

result = []

for i in data:
  if i not in result:
    result.append(i)

result.sort()
print(*result, end = " ")
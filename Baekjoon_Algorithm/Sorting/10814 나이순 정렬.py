# 문제 https://www.acmicpc.net/problem/10814
n = int(input())

data = [] 
for _ in range(n):
  age, name = input().split()
  data.append((int(age),name))

# key 기준으로 정렬
data = sorted(data, key= lambda data: data[0])

for i in data:
  print(*i)
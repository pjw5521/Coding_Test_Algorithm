# https://www.acmicpc.net/problem/14501
n = int(input())

t = []
p = []

for _ in range(n):
  a, b = map(int,input().split())
  t.append(a)
  p.append(b)

d = [0] * (n+1)

for i in range(n-1, -1 ,-1):
  # i번째에 일을 하는 게 n을 초과하면 일을 하지 않음 
  if t[i] + i > n:
      d[i] = d[i+1]
  # i번째에 일을 하는 것과 일을 안하는 것 중 최댓값 
  else:
    d[i] = max(d[i+1], p[i] + d[i +t[i]])

print(d[0])
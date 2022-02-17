# https://www.acmicpc.net/problem/6064
t = int(input())

for _ in range(t):
  m, n, x, y = map(int,input().split())

  result = True
  
  while x <= m * n :
    if (x-y) % n == 0:
      print(x)
      result = False
      break
    x += m

  if result : 
    print(-1)
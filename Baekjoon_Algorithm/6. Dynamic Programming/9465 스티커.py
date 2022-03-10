# https://www.acmicpc.net/problem/9465
t = int(input())

for _ in range(t):
  n = int(input())

  data = []
  for _ in range(2):
    data.append(list(map(int,input().split())))

  for i in range(1,n):
    if i == 1 :
      data[0][i] += data[1][0]
      data[1][i] += data[0][0]
    else:
      data[0][i] += max(data[1][i-1], data[1][i-2])
      data[1][i] += max(data[0][i-1], data[0][i-2])

  print(max(data[0][n-1], data[1][n-1]))

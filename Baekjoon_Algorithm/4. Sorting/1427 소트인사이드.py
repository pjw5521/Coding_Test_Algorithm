# https://www.acmicpc.net/problem/1427

data = list(map(int,input()))

data.sort(reverse = True)

for i in data:
  print(i,end="")
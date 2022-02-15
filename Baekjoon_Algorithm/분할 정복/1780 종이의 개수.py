# https://www.acmicpc.net/problem/1780﻿
result = []
def sol(x, y, n):
  start = graph[x][y]
  
  for i in range(x, x+n):
    for j in range(y, y+n):
      # 종이가 같은 수가 아니면 
      if graph[i][j] != start :
        sol(x, y, n//3)
        sol(x, y + n//3, n//3)
        sol(x, y +2 * (n//3) , n//3)
        
        sol(x + n//3, y, n//3)
        sol(x + n//3, y + n//3 , n//3)
        sol(x + n//3, y + 2 * (n//3), n//3)

        sol(x + 2 * (n//3), y, n//3)
        sol(x + 2 * (n//3), y + n//3, n//3)
        sol(x + 2 * (n//3), y + 2 * (n//3), n//3)
        return 
  
  if start == -1:
    result.append(-1)
  if start == 0:
    result.append(0)
  if start == 1 :
    result.append(1)
    
n = int(input())

graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

sol(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
# https://www.acmicpc.net/problem/1992
result = []

def sol(x,y,n):
  start = graph[x][y]
  
  global result 

  for i in range(x, x+n):
    for j in range(y, y+n):
      if start != graph[i][j]:
        result.append('(')
        sol(x, y, n//2)
        sol(x, y+n//2,n//2)
        sol(x+n//2, y, n//2)
        sol(x+n//2, y+n//2, n//2)
        result.append(')')
        return

  if start == 0:
    result.append('0')
  else:
    result.append('1')
    
n = int(input())

graph = []

for _ in range(n):
  graph.append(list(map(int,input())))

sol(0,0,n)
print("".join(result))
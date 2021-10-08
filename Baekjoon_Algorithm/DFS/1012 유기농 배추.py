test_case = int(input())

def dfs(x, y):
  if x<=-1 or x >=n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x+1,y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

for _ in range(test_case):
  m, n, k = map(int,input().split())

  graph = [ [0] * (m) for _ in range(n)] 
 #2차원 리스트로 표현
  for _ in range(k):
    a, b = map(int,input().split())
    graph[b][a]=1

  count = 0
  for i in range(n):
    for j in range(m):
      if dfs(i,j) == True:
        count += 1 

  print(count) 

# 두번 품
from collections import deque

n, m, v = map(int,input().split())

# 2차원 리스트로 표현
graph = [ [0] * (n+1) for i in range(n+1) ]

for i in range(m):
  a, b = map(int,input().split())
  graph[a][b] = graph[b][a] = 1

# for dfs
visited = [False] * (n+1)

def dfs(v):
  visited[v] = True
  print(v,end=" ")
  for i in range(1, n+1):
    if graph[v][i] == 1 and visited[i] == 0:
      dfs(i) 

# for bfs
seened = [False] * (n+1)  
def bfs(v):
  queue = deque()
  queue.append(v)
  seened[v] = True
  while queue:
    v = queue.popleft()
    print(v,end=" ")
    for i in range(1,n+1):
      if graph[v][i] == 1 and seened[i]==0:
        queue.append(i)
        seened[i]=True

dfs(v)
print()
bfs(v)
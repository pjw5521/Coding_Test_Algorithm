# https://www.acmicpc.net/problem/2606
from collections import deque
n = int(input())
m = int(input())

graph = [ [0]* (n+1) for _ in range(n+1)]

for _ in range(m):
  a,b= map(int,input().split())
  graph[a][b] = 1 
  graph[b][a] = 1

q = deque()
q.append(1)

visited = [False] * (n+1)
visited[1] = True
count = 0 
while q :
  v = q.popleft()
  for i in range(1,n+1):
    if graph[v][i] == 1 and visited[i] == False:
      visited[i] = True
      q.append(i)
      count += 1 

print(count)
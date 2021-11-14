# https://www.acmicpc.net/problem/11724
from collections import deque
import sys 

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [ [0]*(n+1) for _ in range(n+1) ]

dx = [ -1 ,0, 1, 0 ]
dy = [ 0, -1, 0, 1 ]

for _ in range(m):
  a, b= map(int,input().split())
  graph[a][b] = graph[b][a] = 1

q = deque()


visited = [False] * (n+1)

def bfs(start):
  q.append(start)
  visited[start] = True
  while q :
    v = q.popleft()
    for i in range(1,n+1):
      if graph[v][i] == 1 and visited[i] == False:
        visited[i] = True
        q.append(i)

count =0
for i in range(1, n+1):
  if not visited[i] :
    bfs(i)
    count += 1 

print(count)

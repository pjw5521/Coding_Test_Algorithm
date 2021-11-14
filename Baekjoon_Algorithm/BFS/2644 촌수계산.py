#https://www.acmicpc.net/problem/2644

from collections import deque
import sys
input = sys.stdin.readline 

n = int(input())

s, e = map(int,input().split())

m = int(input())

graph = [ [0] * (n+1) for _ in range(n+1) ]

for _ in range(m):
  a, b = map(int,input().split())
  graph[a][b] = graph[b][a] = 1

visited = [0] * (n+1)

q = deque()
q.append(s)

while q:
  v = q.popleft()
  for i in range(1, n+1):
    if graph[v][i] == 1 and visited[i]== 0:
      visited[i] = visited[v]+ 1
      q.append(i)

if visited[e] == 0:
  print (-1)
else:
  print(visited[e])
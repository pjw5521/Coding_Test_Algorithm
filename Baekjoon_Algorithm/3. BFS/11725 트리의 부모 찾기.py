# https://www.acmicpc.net/problem/11725
from collections import deque
import sys
input = sys.stdin.readline 

n = int(input())

graph = [ [] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
  
root = [0] * (n+1)
visited = [False] * (n+1)
q = deque()
q.append(1)

while q:
  v = q.popleft()
  for i in graph[v]:
    if visited[i] == False:
      root[i] = v
      q.append(i)
      visited[i] = True

for i in range(2,n+1):
  print(root[i])

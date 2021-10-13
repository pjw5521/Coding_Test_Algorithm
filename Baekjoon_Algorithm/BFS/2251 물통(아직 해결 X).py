#문제 https://www.acmicpc.net/problem/2251
# 이해안돼서 못품 
from collections import deque
a, b, c = map(int, input().split())
visited = [ [False] * (b+1) for _ in range(a+1)]
ans = []

def pour(x,y):
  if not visited[x][y] :
    visited[x][y] = 1
    
def bfs(x, y,z):
  q = deque()
  q. append((0,0))
  visited[0][0] = True
  while q:
    x, y = q.popleft()
    z = c - x - y 
    if x == 0 :
      ans.append(x)
    if x > 0 and y < b :
      w = min(x, b-y)
      pour 

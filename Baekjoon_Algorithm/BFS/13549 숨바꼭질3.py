# https://www.acmicpc.net/problem/13549
from collections import deque
import sys
input = sys.stdin.readline 
n, k = map(int,input().split())

dist = [-1] * (10**5 + 1)

dist[n] = 0 

queue = deque()
queue.append(n)
while queue:
  x = queue.popleft()
  if x == k:
    print(dist[x]) 
    break
  if 0 <= x-1 <= 10**5 and dist[x-1] == -1: 
    dist[x-1] = dist[x] + 1 
    queue.append(x-1)
  if 0 < x*2 <= 10**5 and dist[x*2] == -1:
      dist[x*2] = dist[x] 
      queue.appendleft(x*2)
  if 0 <= x+1 <= 10**5 and dist[x+1] == -1: 
      dist[x+1] = dist[x] + 1 
      queue.append(x+1)



# https://www.acmicpc.net/problem/12851
from collections import deque 

n, k = map(int,input().split())

cnt = 0 
visited = [-1] * 100001
visited[n] = 0 
q = deque()
q.append(n)

while q :
  x = q.popleft()
  if x ==k :
    cnt += 1 
  for i in (x+1, x-1, x*2):
    if 0 <= i <= 100000:
      if visited[i] == -1 or visited[i] >= visited[x] + 1:
        visited[i] = visited[x] + 1
        q.append(i)

print(visited[k])
print(cnt)
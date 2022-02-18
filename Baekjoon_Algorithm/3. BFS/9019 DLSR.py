# https://www.acmicpc.net/problem/9019
from collections import deque 
import sys
input = sys.stdin.readline 

t = int(input())

def bfs(s):
  
  visited[s] = True
  
  q = deque()
  q.append((s,""))
  
  while q:
    num, c = q.popleft()
    if num == b:
      return c
      
    if num * 2 > 9999 :
      if not visited[(2* num) % 10000] :
        visited[(2* num) % 10000] = True
        q.append(((2* num) % 10000 , c +"D" ))
    else :
      if not visited[num*2]:
        visited[num*2] = True
        q.append((num*2 , c+"D"))

    if num == 0:
      if not visited[9999]:
        visited[9999] = True
        q.append((9999, c + "S"))
    else :
      if not visited[num-1]:
        visited[num-1] = True
        q.append((num - 1 , c + "S"))

    nx = int((num%1000)*10 + num / 1000)
    ny = int((num%10)*1000 + num / 10)
    if num != 0:
      if not visited[nx]:
        visited[nx] = True
        q.append((nx, c + "L"))
    
      if not visited[ny]:
        visited[ny] = True
        q.append((ny, c + "R"))

for _ in range(t):
  a, b = map(int,input().split())
  visited = [False] * 10000
  print(bfs(a))
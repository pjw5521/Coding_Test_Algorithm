# 문제 https://www.acmicpc.net/problem/2251
from collections import deque

# 중복 방지 
def isvisited(a1, b1):
  if visited[a1][b1] == 0:
    visited[a1][b1] = 1
    q.append([a1,b1])

# 물을 옮길 수 있는 경우 a->b,a->c, b->a, b->c, c->a, c->b 6가지 
def bfs():
  while q:
    a1, b1 = q.popleft()
    c1 = c - a1 - b1
    if a1 == 0: # a 물통이 비어있을 때 c의 물의 양 
      result.append(c1)
    # a -> b 
    if a1 + b1 < b :
      isvisited(0, a1+b1)
    else:
      isvisited(a1 - (b - b1), b)
    # a -> c
    if a1 + c1 < c:
      isvisited(0, b1)
    else:
      isvisited(a1 - (c -c1), b1)
    #b->a
    if a1 + b1 < a:
      isvisited(a1+b1,0)
    else:
      isvisited(a, b1 - (a-a1))
    #b->c
    if b1+c1 < c:
      isvisited(a1, 0)
    else:
      isvisited(a1, b1 - (c-c1))
    # c->a
    if c1+a1 < a:
      isvisited(a1+c1,b1)
    else:
      isvisited(a, b1)
    # c->b
    if b1 + c1 < b:
      isvisited(a1, b1+c1)
    else:
      isvisited(a1, b)

a,b,c = map(int,input().split())

MAX = 201
visited = [ [0] * MAX for _ in range(MAX)] # a와 b에 남아있는 물의 양 
visited[0][0] = 1 

q = deque()
q.append([0,0])

result = []
bfs()
result.sort()
print(*result)

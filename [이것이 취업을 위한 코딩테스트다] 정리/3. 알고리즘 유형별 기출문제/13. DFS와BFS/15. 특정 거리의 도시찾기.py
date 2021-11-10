# 문제 339쪽 
# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
sys.setrecursionlimit(100000) # 이거 추가안해주면 런타임 에러. pypy3으로 하면 안됨 
input = sys.stdin.readline # input()으로 받으면 메모리 초과 

n, m, k, x = map(int,input().split())

graph= [ [] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0 

q = deque([x])
while q:
  now = q.popleft()
  for next_node in graph[now]:
    if distance[next_node] == -1:
      distance[next_node] = distance[now] + 1 
      q.append(next_node)

check = False
for i in range(1,n+1):
  if distance[i] == k :
    print(i)
    check = True

if check == False:
  print("-1")
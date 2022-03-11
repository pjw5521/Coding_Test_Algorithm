# https://www.acmicpc.net/problem/15686
from itertools import combinations 
import sys
input = sys.stdin.readline 

n, m = map(int,input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int,input().split())))

chick = []
home = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 2:
      chick.append((i,j))
    if graph[i][j] == 1 :
      home.append((i,j))
      
combine = list(combinations(chick, m))
answer = int(1e9)

for i in combine :
  result = 0 
  for b in home :
    tmp = int(1e9)
    for a in i :
      tmp = min(tmp, abs(b[0]-a[0]) + abs(b[1]-a[1]))
    result += tmp 

  if result < answer :
    answer = result 
      
print(answer)
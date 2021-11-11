# https://www.acmicpc.net/problem/1446
from collections import defaultdict
import sys
input = sys.stdin.readline

n, d = map(int,input().split())
# 유사 딕셔너리 
graph = defaultdict(list)
distance = [ i for i in range(d+1) ] 

for _ in range(n):
  # 시작위치, 도착위치, 거리
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

for i in range(d+1) : 
  if i > 0:
    distance[i] = min(distance[i],distance[i-1] + 1 )
  if i in list(graph):
    for v,w in graph[i]:
      # 지름길을 거쳐서 가는게 더 빠를 때 
      if v <= d and distance[v] > distance[i] + w:
        distance[v] = distance[i] + w 
  
print(distance[d])


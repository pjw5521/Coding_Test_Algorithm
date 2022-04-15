# https://www.acmicpc.net/problem/1766
from collections import deque 
import heapq 

n, m = map(int,input().split())

graph = [ [] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1 
    
q = []
# 우선 순위 큐에 넣기 
for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q,i)
        
ans = []

# 위상 정렬 알고리즘 
while q:
    now  = heapq.heappop(q)
    ans.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1 
        if indegree[i] == 0:
            heapq.heappush(q,i)

print(*ans)
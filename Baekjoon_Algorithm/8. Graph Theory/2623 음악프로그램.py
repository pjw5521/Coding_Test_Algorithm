# https://www.acmicpc.net/problem/2623
from collections import deque

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q :
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1 
            
            if indegree[i] == 0 :
                q.append(i)

    if len(result) != n:
        print(0)
    else:
        for i in result:
            print(i)
    
n, m = map(int,input().split())

indegree = [0] * (n+1)
graph = [ [] for _ in range(n+1) ] 

for _ in range(m):
    seq = list(map(int,input().split()))
    for i in range(1, len(seq)-1):
        graph[seq[i]].append(seq[i+1])
        indegree[seq[i+1]] += 1 
        
topology_sort()
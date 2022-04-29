# https://www.acmicpc.net/problem/2617
from collections import defaultdict, deque

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    q = deque()
    q.append(start)
    cnt = 0 
    
    while q:
        x = q.popleft()

        for i in heavy[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1 
        
        if cnt > n // 2 :
            return True 
        
    visited  = [False] * (n+1)
    
    visited[start] = True
    q = deque()
    q.append(start)
    cnt = 0 
    while q:
        x = q.popleft()

        for i in light[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1 
        
        if cnt > n // 2 :
            return True 
            
    return False 
    
n, m = map(int,input().split())

heavy = defaultdict(list)
light = defaultdict(list)

for _ in range(m):
    a, b = map(int,input().split())
    # b보다 무거운 거
    heavy[b].append(a)
    # a보다 가벼운 거
    light[a].append(b)


answer = 0 

for i in range(1,n+1):
    if bfs(i):
        answer += 1 

print(answer)
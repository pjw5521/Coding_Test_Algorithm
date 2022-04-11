# https://www.acmicpc.net/problem/5014
from collections import deque 

def bfs(start):
    visited[start] = True 
    
    q = deque()
    q.append((start, 0))

    while q :
        x, cnt = q.popleft()
        
        # g에 도착했으면 
        if x == g :
            return cnt 
            
        # 아래로 이동할 수 있으면 
        if (x - d > 0 and not visited[x-d]) :
            q.append((x-d, cnt + 1 ))
            visited[x-d] = True
        # 위로 이동할 수 있으면 
        if (x + u < f + 1 and not visited[x+u]) :
            q.append((x+u,cnt+1))
            visited[x+u] = True
    
    return -1 
            
f, s, g, u, d = map(int,input().split())

visited = [False] *  (f + 1)
visited[s] = True
result = bfs(s)

if result == -1:
    print("use the stairs")
else:
    print(result)
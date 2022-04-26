# https://www.acmicpc.net/problem/15649
# 백트래킹 
def dfs(s):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return 
    for i in range(1,n+1):
        if visited[i]:
            continue 

        visited[i] = True 
        s.append(i)
        dfs(s)
        s.pop()
        visited[i] = False 
        
n, m = map(int,input().split())

stack = [] 
visited = [False] * (n+1)
dfs(stack)
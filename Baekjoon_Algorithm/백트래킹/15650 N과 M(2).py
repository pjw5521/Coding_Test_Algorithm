# https://www.acmicpc.net/problem/15650
def dfs(num, s):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return 
        
    for i in range(num,n+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(i,s)
            s.pop()
            visited[i]=False
            
n, m = map(int,input().split())

visited = [False] * (n+1)
s = []
dfs(1, s)
# https://www.acmicpc.net/problem/15652
def dfs(num,s):
  if len(s) == m:
    print(" ".join(map(str,s)))
    return
  
  for i in range(num,n+1):
    s.append(i)
    dfs(i,s)
    s.pop()
    
n, m = map(int,input().split())
s = []
dfs(1, s)


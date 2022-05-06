# https://www.acmicpc.net/problem/1520
import sys 
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

def sol(x, y):
	# 오른쪽 맨 끝 도착했으면 1 리턴 
    if x == m-1 and y == n-1:
        return 1 
    
    # 이미 방문했던 곳이면 저장된 경로의 수 바로 리턴 
    if dp[x][y] != -1:
        return dp[x][y]
        
    cnt = 0 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n  and graph[x][y] > graph[nx][ny]:
            cnt += sol(nx,ny)
    
    # 경로 수 갱신     
    dp[x][y] = cnt 
    
    return dp[x][y]   
        
m, n = map(int,input().split())

graph = []
dp = [ [-1] * n for _ in range(m) ]
for _ in range(m):
    graph.append(list(map(int,input().split())))
    
print(sol(0,0))

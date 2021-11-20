import sys
sys.setrecursionlimit(100000) # 이거 추가안해주면 런타임 에러. pypy3으로 하면 안됨 
r = sys.stdin.readline # input()으로 받으면 메모리 초과 

n = int(r())

graph = []
for _ in range(n):
  graph.append(list(map(int,r().split())))


dx = [ 1, -1, 0, 0 ]
dy = [ 0 , 0,-1, 1 ]

def dfs(x, y, k):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0 <= nx < n) and ( 0<= ny < n) and not visited[nx][ny] and graph[nx][ny] > k:
      visited[nx][ny] = True
      dfs(nx, ny ,k)

ans =1
for k in range(max(map(max,graph))):
  visited = [ [False] * n for _ in range(n)]
  safe = 0 
  for i in range(n):
    for j in range(n):
      if graph[i][j] > k and not visited[i][j]:
        visited[i][j] = True
        safe += 1
        dfs(i, j, k)
  ans= max(ans, safe)

print(ans)
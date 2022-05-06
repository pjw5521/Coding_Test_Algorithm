# https://www.acmicpc.net/problem/11562
n, m = map(int,input().split())

INF = int(1e9)
graph = [ [INF] * (n+1) for _ in range(n+1)] 

for _ in range(m):
    a, b, c = map(int,input().split())
    if c == 0 :
        graph[a][b] = 0
        # 일방통행이므로 지나가는데 드는 비용이 1 
        graph[b][a] = 1 
    else:
        graph[a][b] = 0
        graph[b][a] = 0 
  
# 자기 자신으로 가는 비용 0으로 초기화 
for i in range(1,n+1) :
    for j in range(1,n+1):
        if i == j :
            graph[i][j] = 0 
     
# 최소 통로 건설 개수 구하기 
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
          
k = int(input())
for _ in range(k):
    x, y = map(int,input().split())
    print(graph[x][y])
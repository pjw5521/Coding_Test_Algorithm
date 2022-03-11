# https://www.acmicpc.net/problem/11404
n = int(input())

m = int(input())
INF = int(1e9)

graph = [ [INF] * (n+1) for _ in range(n+1) ]

for _ in range(m):
  a, b, c = map(int,input().split())
  # 시작 도시와 도착 도시를 연결하는 노선이 하나가 아닐 수 있으므로 
  if graph[a][b] < INF:
    graph[a][b] = min(graph[a][b], c)
  else:
    graph[a][b] = c

# 자기자신에서 자기 자신으로 가는 비용 0으로 초기화 
for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0 
      
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    # 갈 수 없는 경우 
    if graph[i][j] == INF:
      print(0,end = " ")
    else:
      print(graph[i][j], end = " ")
  print()
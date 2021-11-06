# 문제 259쪽 
# 1번에서 K를 거쳐 x까지의 최단 거리는 [1에서 k까지 최단거리] + [k에서 x까지 최단거리]
n, m = map(int,input().split())
INF = int(1e9)
graph = [ [INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신의 비용은 0
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b] = 0

# 정보 입력 받아 넣기 
for _ in range(m):
  a,b = map(int,input().split())
  graph[a][b] = 1
  graph[b][a] = 1 

x, k = map(int,input().split())

# 플로이드 워셜 알고리즘 
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print("-1")
else :
  print(distance)
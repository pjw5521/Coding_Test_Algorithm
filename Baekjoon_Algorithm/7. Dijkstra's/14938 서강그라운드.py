# https://www.acmicpc.net/problem/14938
n, m, r = map(int,input().split())

item = list(map(int,input().split()))

INF = int(1e9)

graph = [ [INF] * (n+1) for _ in range(n+1) ]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j] = 0

for _ in range(r):
  a,b,c = map(int,input().split())
  graph[a][b] = c 
  graph[b][a] = c 

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for i in range(1,n+1):
  result = 0 
  # 예은이가 떨어진 지역에서 다른 지역까지의 거리가 수색 범위에 속하면 
  for j in range(1,n+1):
    if graph[i][j] <= m:
      # 해당 지역의 아이템 추가 
      result += item[j-1]
   # 최댓값 갱신 
  answer = max(answer,result)

print(answer)
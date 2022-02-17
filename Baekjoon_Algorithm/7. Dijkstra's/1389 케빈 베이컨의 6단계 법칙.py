# https://www.acmicpc.net/problem/1389
INF = int(1e9)
n , m = map(int,input().split())

graph = [[INF] * n for _ in range(n)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화 
for a in range(n):
  for b in range(n):
    if a == b :
      graph[a][b] = 0

# a와 b가 친구라면 1로 표시 
for _ in range(m):
  a,b = map(int,input().split())
  graph[a-1][b-1] = 1
  graph[b-1][a-1] = 1

# 플로이드 워셜 점화식 
for k in range(n):
  for i in range(n):
    for j in range(n):
      graph[i][j] = min(graph[i][j],(graph[i][k]+ graph[k][j]))

result = INF

# 각 사람별 단계의 총합을 구해 케빈 베이컨 수의 가장 작은 값을 저장 
for i in graph:
  result = min(result,sum(i))

# 케빈 베이컨의 수가 가장 작은 사람의 번호 출력 
for i in range(n):
  if result == sum(graph[i]):
    print(i+1)
    break
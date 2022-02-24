# https://www.acmicpc.net/problem/11660import sys
input = sys.stdin.readline 
  
n, m = map(int,input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int,input().split())))

num_sum = [ [0] * (n+1) for _ in range(n+1)]

# 누적합 구하기 
for i in range(1,n+1):
  for j in range(1,n+1):
    num_sum[i][j] = graph[i-1][j-1] + num_sum[i-1][j] + num_sum[i][j-1] - num_sum[i-1][j-1]

for _ in range(m):
  x1, y1, x2, y2 = map(int,input().split())
  
  result = num_sum[x2][y2] - num_sum[x1 - 1][y2] - num_sum[x2][y1 - 1] + num_sum[x1 - 1][y1 - 1]

  print(result)
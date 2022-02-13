# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, b = map(int,input().split())

graph = []

for i in range(n):
  graph.append(list(map(int,input().split())))

# 걸리는 시간 
answer = INF
# 높이
h = 0 
 
for i in range(257):
  # b_min : 인벤토리에서 뺄 블록 수 
  # b_max : 인벤토리에 넣을 블록 수
  b_min = 0
  b_max = 0

  for x in range(n):
    for y in range(m):
      # 맞출 높이보다 작을 때 블록을 좌표에 놓아야 한다 
      if i > graph[x][y] :
        b_min += (i - graph[x][y])
      # 맞출 높이보다 크면 블록을 인벤토리에 넣어야 한다 
      else :
        b_max += (graph[x][y] - i) 
  # 총 블록 수 
  block = b + b_max 
  # 블록수가 부족하면 
  if block < b_min :
    continue
  # 걸리는 시간 계산 
  t = 2 * b_max + b_min
  # 시간 작은 값으로 갱신, 같을 경우 높이가 높은 것으로 갱신 
  if t <= answer :
    answer = t 
    h = i 
    
print(answer, h)
# https://www.acmicpc.net/problem/1018
n, m = map(int,input().split())

graph = []
# 다시 칠해야 하는 정사각형의 개수는 최대 64 
answer = 64 

for _ in range(n):
  graph.append(list(map(str,input())))

# 8 * 8 체스판을 만들 수 있는 모든 경우의 수에 대하여 탐색 
for i in range(n-7):
  for j in range(m-7):
    w_cnt = 0 # (0,0) 위치가 w로 시작할 때 다시 칠해야하는 판의 개수
    b_cnt = 0 # (0,0) 위치가 b로 시작할 때 다시 칠해야 하는 판의 개수 
    
    for x in range(8):
      for y in range(8):
        index = (x+y) % 2 
        if index == 0:
          # (0,0) 위치가 w로 시작할 때 : w가 아니면 다시 칠해야 하므로 w_cnt + 1 
          if graph[i+x][j+y] != 'W':
            w_cnt += 1 
          # (0,0) 위치가 b로 시작할 때 : b가 아니면 다시 칠해야 하므로 b_cnt + 1 
          if graph[i+x][j+y] != 'B':
            b_cnt += 1
        else:
          # (0,0) 위치가 w로 시작할 때 : b가 아니면 다시 칠해야 하므로 w_cnt + 1 
          if graph[i+x][j+y] != 'B': 
            w_cnt += 1 
          # (0,0) 위치가 b로 시작할 때 : w가 아니면 다시 칠해야 하므로 b_cnt + 1 
          if graph[i+x][j+y] != 'W':
            b_cnt += 1
    # 칠해야 하는 체스판의 개수가 작은 것으로 갱신 
    answer = min(answer, b_cnt, w_cnt)

print(answer)
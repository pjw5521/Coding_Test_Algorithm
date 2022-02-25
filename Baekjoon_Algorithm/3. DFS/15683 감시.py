# https://www.acmicpc.net/problem/15683
import copy

dx = [ -1, 0, 1, 0 ]
dy = [ 0, -1, 0, 1 ]

INF = int(1e9)
# cctv 별 바라볼 수 있는 방향  
mode = [
  [],
  [[0],[1],[2],[3]],
  [ [1,3], [0,2]],
  [ [0,3], [2,3], [1,2], [0,1] ],
  [ [0,1,2], [1,2,3], [0,2,3], [0,1,3]],
  [ [0,1,2,3]]
]

# 감시할 수 있는 곳 7로 변환하는 함수 
def check(board, dir, x, y):
  for i in dir:
    nx = x
    ny = y

    while True:
      nx += dx[i]
      ny += dy[i]
      # 범위에서 벗어나거나 벽을 만나면 중단 
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        break
      if board[nx][ny] == 6:
        break
      # 7로 변환 
      if board[nx][ny] == 0:
        board[nx][ny] = 7 
        
def dfs(cnt,arr):
  global answer 

  # 모든 cctv의 감시할 수 있는 곳을 검사했으면 
  if cnt == len(cctv):
    count = 0 
    # 남은 0의 개수 계산 
    for i in range(n):
      count += arr[i].count(0)
    
    # 최솟값 갱신 
    answer = min(answer,count)
    return 
  
  # 그래프 복사 
  tmp = copy.deepcopy(arr)
  # cctv 종류와 위치 
  cctv_num, x, y = cctv[cnt]
  
  # cctv가 모든 바라볼 수 있는 방향에 대하여 
  for i in mode[cctv_num]:
    check(tmp,i,x,y)
    dfs(cnt+1, tmp)
    tmp = copy.deepcopy(arr)
    
n, m = map(int,input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int,input().split())))

cctv = []
for i in range(n):
  for j in range(m):
    # cctv 종류와 위치 저장 
    if graph[i][j] != 0 and graph[i][j] != 6:
      cctv.append((graph[i][j],i,j))

answer = INF
dfs(0,graph)
print(answer)
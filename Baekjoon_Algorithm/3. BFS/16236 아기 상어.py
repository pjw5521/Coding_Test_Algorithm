# https://www.acmicpc.net/problem/16236
from collections import deque 

INF = int(1e9)
dx = [ 1, -1 ,0 ,0 ]
dy = [ 0, 0, 1, -1 ]

def bfs(a, b):
  q = deque()
  # (위치, 현재 위치에서 이동거리)
  q.append((a,b,0))
  
  visited = [ [False] * n for _ in range(n)]
  # 현재 아기 상어의 위치 방문 표시 
  visited[a][b] = True

  # 먹을 수 있는 물고기 리스트 
  dist_list = []
  
  while q :
    x, y, dist = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위에 속하고 방문하지 않았으면 
      if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
        # 아기 상어의 크기보다 작거나 같으면 이동 가능 
        if graph[nx][ny] <= size:
          # 방문 표시하고 거리 +1 하여 큐에 삽입 
          visited[nx][ny]=True
          q.append((nx,ny,dist+1))
          # 0이 아니고 아기 상어의 크기보다 작으면 먹을 수 있는 물고기이므로
          if 0< graph[nx][ny] < size:
            # 먹을 수 있는 물고기에 추가 
            dist_list.append((dist+1, nx, ny))
          
  # 먹을 수 있는 물고기가 있으면 
  if dist_list:
    # 이동거리, x좌표, y좌표 순으로 정렬 
    dist_list.sort(key = lambda x :(x[0],x[1],x[2]))
    # 가장 가까운 물고기 정보 전달 
    return dist_list[0]
  # 먹을 수 있는 물고기가 없다면 
  else:
    return False 

n = int(input())

graph = []

q = deque ()
# 물고기의 개수 저장할 변수 
fish_cnt = 0

# 아기 상어의 위치 저장할 변수
sx, sy = 0, 0
for _ in range(n):
  graph.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    # 물고기 개수 저장 
    if 0 < graph[i][j] <= 6:
      fish_cnt += 1 
    # 아기 상어의 위치 저장 
    if graph[i][j] == 9:
      graph[i][j] = 0
      sx = i
      sy = j

# 아기 상어 크기
size = 2
# 먹은 물고기 개수 
eat = 0
# 총 이동 거리 
answer = 0 

# 먹을 물고기가 있으면 
while fish_cnt :
  
  result = bfs(sx,sy)

  # 먹을 수 있는 물고기가 없다는 뜻이므로 
  if not result:
    break
  # 먹은 물고기의 위치로 아기 상어 위치 이동 
  sx = result[1]
  sy = result[2]

  # 이동 거리 더하기 
  answer += result[0]

  # 먹은 물고기의 개수 증가
  eat += 1 
  # 남은 물고기의 개수 감소 
  fish_cnt -= 1

  # 먹은 물고기의 개수와 아기 상어의 크기가 같다면 
  if size == eat :
    # 아기 상어 크기 증가
    size += 1
    # 먹은 물고기의 개수 초기화 
    eat = 0

  # 먹은 물고기의 크기 0으로 
  graph[sx][sy] = 0

# 총 이동 거리 = 총 걸린 시간 
print(answer)
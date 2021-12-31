# bfs로 풀이 
from collections import deque

def solution(places):
    answer = []
    for i in places:
      answer.append(bfs(i))
    return answer

def bfs(graph):

  dx = [ 1, -1, 0, 0 ]
  dy = [ 0, 0, 1, -1 ]
  
  start = []
  # p의 위치 저장. 
  for i in range(5):
    for j in range(5):
      if graph[i][j] == 'P':
        start.append((i,j))
   
  #p의 위치마다 검사 
  for a,b in start :
    q = deque()
    # 방문 기록 초기화 
    visited = [ [0]*5 for _ in range(5) ]
    # 거리 초기화 
    distance = [ [0] * 5  for _ in range(5) ]

    q.append((a,b))
    visited[a][b] = 1
    
    while q:
      x, y = q.popleft()
      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위에 맞고 아직 방문하지 않았으면 
        if ( 0 <= nx < 5 ) and ( 0 <= ny < 5 ) and visited[nx][ny] == 0:
          # 벽이 아니라면 방문 기록, 거리 갱신 
          if graph[nx][ny] == 'O':
            q.append((nx,ny))
            visited[nx][ny] = 1
            distance[nx][ny] = distance[x][y] + 1 
          # 응시자를 만났다면 거리 확인, 거리가 1보다 작거나 같으면 거리두기 실패 
          elif graph[nx][ny] == 'P' and distance[x][y] <=1 :
            return 0
    
  return 1
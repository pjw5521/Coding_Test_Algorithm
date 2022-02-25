# https://www.acmicpc.net/problem/13460
from collections import deque 

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

def move(x,y,mx,my):
  m_count = 0 
  while graph[x+mx][y+my] != '#':
    if graph[x+mx][y+my] =='O':
      return 0, 0, 0
    x += mx
    y += my
    m_count += 1 

  return x, y, m_count
  
def bfs(rx,ry,bx,by):
  visited = {}
  # 방문 표시, 굴린 횟수 0 
  visited[rx,ry,bx,by] = 0 

  q = deque()
  q.append((rx,ry,bx,by))

  while q :
    
    rx, ry, bx, by = q.popleft()

    # 굴린 횟수가 10 이상이면 
    if visited[rx,ry,bx,by] >= 10 :
      print(-1)
      return 

    for i in range(4):
      # 한 방향으로 굴리기 
      nrx, nry, rmove = move(rx,ry,dx[i],dy[i])    
      nbx, nby, bmove = move(bx,by,dx[i],dy[i])

      # 두 공 모두 탈출했거나 파란 공만 탈출한 경우 무시 
      if not nbx and not nby :
        continue
      # 빨간 공만 탈출한 경우 
      elif not nrx and not nry:
        # 굴린 횟수 출력 
        print(visited[rx,ry,bx,by]+1)
        return 
      # 빨간 공과 파란 공의 위치가 같다면 
      elif nrx == nbx and nry == nby :
        # 더 많이 이동한 공 한칸 뒤로 이동 
        if rmove > bmove:
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]
      # 방문 기록 표시 
      if (nrx,nry,nbx,nby) not in visited :
        visited[nrx,nry,nbx,nby] = visited[rx,ry,bx,by]+1
        q.append((nrx,nry,nbx,nby))
  # 리턴하지 않고 끝났다면 구멍을 통해 빼낼 수 없다는 뜻이므로
  print(-1)
  return 
    
n, m = map(int,input().split())

graph = []

for _ in range(n):
  graph.append(list(input()))

# 처음 빨간 공, 파란 공 위치 기록 
rx, ry, bx, by = 0,0,0,0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'R':
      rx = i
      ry = j
    if graph[i][j] == 'B':
      bx = i
      by = j

bfs(rx,ry,bx,by)
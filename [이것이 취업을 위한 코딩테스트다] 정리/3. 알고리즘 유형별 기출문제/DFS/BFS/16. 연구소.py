# 문제 341쪽
# https://www.acmicpc.net/problem/14502
# 벽을 놓을 수 있는 모든 경우의 수에 대하여 안전 지대 구함 
from collections import deque
import sys
import copy

input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [ -1, 0, 1, 0 ]
dy = [ 0, -1, 0, 1 ]
ans = 0

def bfs():
  global ans
  # 임시 그래프 
  w = copy.deepcopy(a)
  # 바이러스가 있는 곳 위치 저장 
  for i in range(n):
    for j in range(m):
      if w[i][j] == 2:
        q.append([i, j])

  while q :
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0<= ny < m and w[nx][ny] == 0:
        q.append([nx,ny])
        w[nx][ny] = 2 

  cnt = 0
  # 0인 곳 개수 구함 
  for i in w:
    cnt += i.count(0)
  ans = max(ans, cnt)

# 벽 놓을 곳 3군데 선택 
def wall(x):
    # 3개 선택했으면 안전 지대 구함 
  if x == 3:
      bfs()
      return
  for i in range(n):
    for j in range(m):
      if a[i][j] == 0:
        a[i][j] = 1
        wall(x+1)
        a[i][j] = 0

wall(0)
print(ans)
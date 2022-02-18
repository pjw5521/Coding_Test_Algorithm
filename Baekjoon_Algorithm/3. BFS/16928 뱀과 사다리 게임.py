# https://www.acmicpc.net/problem/16928
from collections import deque 

def bfs(a):
  visited[a] = True

  q = deque()
  # 도착한 칸과 주사위를 던진 횟수 
  q.append((a,0))

  while q :
    x, cnt  = q.popleft()
    # 100에 도착했으면 주사위를 던진 횟수 return 
    if x == 100:
      return cnt
    # 사다리가 있는 칸이면 사다리를 타고 이동 
    if ladder.get(x) :
        x = ladder[x]
    # 뱀이 있는 칸이면 뱀을 타고 이동 
    if snake.get(x) :
        x = snake[x]
    # 1부터 6까지 주사위를 굴려 나온 수만큼 이동한 칸마다 방문 하지 않았으면 방문 표시하고 주사위 던진 횟수 +1 하여 큐에 삽입 
    for i in range(1,7):
      if x+i <= 100 and not visited[x+i]:
        visited[x+i] = True
        q.append((x+i, cnt + 1))
  
n, m = map(int,input().split())

ladder = dict()
snake = dict()

# 도착한 칸 key, 이동할 칸 value 
for _ in range(n):
  a, b = map(int,input().split())
  ladder[a] = b

for _ in range(m):
  a, b = map(int,input().split())
  snake[a] = b 

visited = [False] * 101

print(bfs(1))
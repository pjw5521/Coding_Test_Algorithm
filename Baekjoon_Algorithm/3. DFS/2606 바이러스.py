# 문제 https://www.acmicpc.net/problem/2606

computer= int(input())
network = int(input())
data = [ [0]* (computer+1) for _ in range(computer+1) ]
visited = [False] * (computer+1)
global count
count = 0 
def dfs(v):
  global count
  visited[v] =True
  for i in range(1, computer+1):
    if data[v][i] == 1 and visited[i] == False:
      count += 1
      dfs(i)
    
for i in range(network):
  x, y = map(int, input().split())
  data[x][y] = 1 
  # 아래 코드 없으면 틀림 
  data[y][x] = 1 

dfs(1)
print(count)

''' bfs 코드 
from collections import deque

c = int(input())

num = int(input())

data = [ [0] * (c+1) for _ in range(c+1)]

for _ in range(num):
  a, b = map(int,input().split())
  data[a][b] = 1
  data[b][a] = 1 

visited = [False] * (c+1)

queue = deque()

queue.append(1)
visited[1] = True

while queue:
  v = queue.popleft()
  for i in range(1,c+1):
    if data[v][i] == 1 and visited[i] == False:
      queue.append(i)
      visited[i] =True

print(visited.count(1)-1)
'''
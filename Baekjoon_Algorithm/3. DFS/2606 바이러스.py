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
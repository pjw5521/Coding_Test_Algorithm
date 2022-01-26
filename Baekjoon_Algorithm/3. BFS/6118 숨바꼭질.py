#https://www.acmicpc.net/problem/6118
from collections import deque, defaultdict

def bfs(v):
  q = deque()
  # 노드 번호와 거리 큐에 삽입 
  q.append((v,0))
  # 1번 노드 방문 기록 표시 
  visited[v] = 1 

  while q:
    x, index = q.popleft()

    for u in maps[x]:
        # 방문하지 않았다면 
      if visited[u] == 0:
        # 거리 하나 증가 
        visited[u] = index+1
        # 큐에 삽입 
        q.append((u, index+1))
  
# 1번 노드로부터 모든 노드까지 최단 거리 구하기 
n, m = map(int,input().split())

maps = defaultdict(list)

for _ in range(m):
  a,b = map(int,input().split())

  maps[a].append(b)
  maps[b].append(a)

visited = [0] * (n+1)
bfs(1)

# 가장 멀리 있는 노드까지의 거리 
answer = max(visited)

# 가장 멀리 있는 노드 중 가장 작은 노드 
for i in range(2,n+1):
  if visited[i] == answer:
    print(i,end =" ")
    break

# 그 헛간까지의 거리 
print(answer, end = " ")

# 그 헛간과 같은 거리를 갖는 헛간의 개수 
print(visited[2:].count(answer))

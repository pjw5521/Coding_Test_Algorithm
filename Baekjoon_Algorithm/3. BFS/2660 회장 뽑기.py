#https://www.acmicpc.net/problem/2660

import collections 

def bfs(v):
  # visited 배열 초기화 
  visited = [0] * (n+1)
  visited[v] = 1 
  
  q = collections.deque()
  q.append((v,0))

  while q :
    t, index = q.popleft()

    for u in maps[t]:
      if visited[u] == 0:
      # 거리 증가 
        visited[u] = index + 1 
        q.append((u,index+1))
  
  # 거리의 최댓값 리턴 
  return(max(visited))

n = int(input())

maps = collections.defaultdict(list)

while True:
  a, b = map(int,input().split()) 

  if a == -1 and b == -1 :
    break
  
  maps[a].append(b)
  maps[b].append(a)

result = collections.defaultdict(int)

for i in range(1,n+1):
  tmp = bfs(i)
  result[i] = tmp

min_num = min(result.values())

print(min_num, end = " ")

answer = []

for i, num in result.items():
  if num == min_num:
    answer.append(i)

answer.sort()

print(len(answer))
print(" ".join(map(str,answer)))
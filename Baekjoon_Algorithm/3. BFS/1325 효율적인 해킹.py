#https://www.acmicpc.net/problem/1325
import collections
import sys
input =  sys.stdin.readline

def bfs(x):
  q = collections.deque()
  q.append(x)
  count = 1
  visited = [False] * (n+1)
  visited[x] = True

  while q:
    v = q.popleft()
    for i in maps[v]:
      if visited[i] == False:
        count += 1 
        visited[i] = True
        q.append(i)

  return count 

n, m = map(int,input().split())

maps = collections.defaultdict(list) 

# b가 a를 해킹할 수 있으므로 
for i in range(m):
  a, b = map(int,input().split())
  maps[b].append(a)

result = []
max_num = 0 

for i in range(1,n+1):
  tmp = bfs(i)
  # 최댓값 저장 
  if max_num < tmp :
    max_num = tmp
  result.append((i,tmp))

for i, count in result:
  if count == max_num:
    print(i, end = " ")
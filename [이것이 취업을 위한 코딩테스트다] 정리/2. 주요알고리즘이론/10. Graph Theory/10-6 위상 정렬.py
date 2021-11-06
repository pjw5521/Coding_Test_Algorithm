from collections import deque

# 노드 개수, 간선의 개수 
v, e = map(int,input().split())

# 모든 노드의 진입차수는 0으로 초기화 
indegree = [0] * (v+1)
graph = [ [] for i in range(v+1) ]

for _ in range(e):
  a, b = map(int,input().split())
  # a에서 b로 이동가능 
  graph[a].append(b)
  # b의 진입차수 +1 
  indegree[b] += 1

def topology_sort():
  # 위상 정렬 수행 결과 
  result = []
  q = deque()

  # 진입 차수 0인 거 큐에 담기 
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수 -1
    for i in graph[now]:
      indegree[i] -= 1
      # 진입 차수 0인거 큐에 담기 
      if indegree[i] == 0:
        q.append(i)
 # 위상정렬 수행 결과 출력 
  for i in result:
    print(i, end = " ")

topology_sort()

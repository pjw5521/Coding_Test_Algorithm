# 문제 303쪽 
from collections import deque
import copy
# 노드 개수, 간선의 개수 
v = int(input())

# 모든 노드의 진입차수는 0으로 초기화 
indegree = [0] * (v+1)
graph = [ [] for i in range(v+1) ]
# 각 강의 시간 
time = [0] * (v+1)

for i in range(1, v+1):
  data = list(map(int, input().split()))
  # 강의 시간 넣기 
  time[i] = data[0]
  for x in data[1:-1]:
    indegree[i] += 1 
    graph[x].append(i)

def topology_sort():
  # 위상 정렬 수행 결과 
  # 리스트 값 복제할 때 deepcopy()
  result = copy.deepcopy(time)
  q = deque()

  # 진입 차수 0인 거 큐에 담기 
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    # 해당 원소와 연결된 노드들의 진입차수 -1
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      # 진입 차수 0인거 큐에 담기 
      if indegree[i] == 0:
        q.append(i)
 # 위상정렬 수행 결과 출력 
  for i in range(1, v+1):
    print(result[i])

topology_sort()

#https://programmers.co.kr/learn/courses/30/lessons/49189
# bfs 풀이 - 시간 초과 
from collections import deque

def solution(n, edge):
    answer = 0
    graph = [ [0]*(n+1) for _ in range(n+1) ]
    
    q = deque()

    distance = [0] * (n+1)

    for a, b in edge:
        graph[a][b] = graph[b][a] = 1 
    
    q.append(1)
    distance[1] = 0
    
    while q :
        v = q.popleft()
        for i in range(1,n+1):
            if graph[v][i] == 1 and distance[i] == 0:
                distance[i] = distance[v] + 1 
                q.append(i)
                
    distance = distance[2:]
    
    return distance.count(max(distance))

# 다익스트라 풀이 
import heapq
INF = int(1e9)

def solution(n, edge):
  graph = [ [] for _ in range(n+1)]
  distance = [INF] * (n+1)

  for c,d in edge:
      graph[c].append((d,1))
      # 양방향으로 해줘야함 
      graph[d].append((c,1)) 

  q = []
  heapq.heappush(q, (0,1))
  distance[1] = 0
  while q :
    # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기 
    dist, now = heapq.heappop(q)
    # 이미 처리된 적이 있으면 무시 
    if distance[now] < dist :
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

  # 0이랑 1번 노드 제외 
  distance = distance[2:]

  return distance.count(max(distance))
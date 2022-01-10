#https://programmers.co.kr/learn/courses/30/lessons/72413
INF = int(1e9)
import heapq

def solution(n, s, a, b, fares):

  graph = [ [] for _ in range(n+1) ]

  # 거리 저장 
  for e1, e2, c in fares:
    graph[e1].append((e2,c))
    graph[e2].append((e1,c))

  answer = INF

  for t in range(1, n+1):
      # 최단 비용 거리 
    answer = min(answer, dijkstra(graph,n,s,t)+dijkstra(graph,n,t,b)+ dijkstra(graph,n,t,a))
    print(answer)

  return answer
  
# 다익스트라 알고리즘 
def dijkstra(graph, n, start, end):

  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0
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

  return distance[end]
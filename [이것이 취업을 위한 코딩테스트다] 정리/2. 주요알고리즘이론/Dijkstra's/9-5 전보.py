# 문제 262쪽
# 다잇스트라 알고리즘 이용 
import heapq
import sys
input = sys.stdin.readline

# 노드개수, 간선개수, 시작 노드 
n, m, start = map(int,input().split())

INF = int(1e9)

graph = [ [] for _ in range(n+1) ]
# 최단 거리 테이블 
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
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

dijkstra(start)

count = 0
max_distance=0

for d in distance:
  if d!= INF:
    # c에서 갈 수 있는 노드의 개수 
    count +=1
    # 도달할 수 있는 노드 중, 가장 멀리 있는 노드와 최단 거리
    max_distance = max(max_distance,d)

# 시작 노드 제외
print(count-1, max_distance)

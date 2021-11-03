# 페이지 237쪽 
import sys 
input = sys.stdin.readline
INF = int(1e9)
# 노드, 간선 개수 
n, m = map(int,input().split())
# 시작 노드 
start = int(input())
# 연결된 노드에 대한 정보
graph = [ [] for i in range(m)]
# 방문한 적이 있는 체크
visited = [False] * (n+1)
# 최단 거리 테이블 
distance = [INF] * (n+1)
# 정보 입력 받음 
for _ in range(m):
# a에서 b로 가는 비용이 c
  a,b,c= map(int,input().split())
  graph[a].append((b,c))

# 방문하지 않은 노드 중 가장 최단 거리 짧은 노드 번호 반환 
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드 초기화 
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    # 노드 start에서 노드 j[0]까지의 거리가 j[1]
    distance[j[0]] = j[1]

  for i in range(n-1):
    now = get_smallest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost
  
dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
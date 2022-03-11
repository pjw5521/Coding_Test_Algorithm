# https://www.acmicpc.net/problem/1167
import heapq 
import sys
input = sys.stdin.readline 

# 다익스트라 알고리즘 
def dijkstra(start):
  distance = [INF] * (v+1)
  distance[start] = 0 

  q = []
  heapq.heappush(q,(0,start))
  while q :
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost,i[0]))

  return distance[1:]
  
v = int(input())

INF = int(1e9)
graph = [ [] for _ in range(v+1) ] 

for _ in range(v):
  s = list(map(int,input().split()))
  index = 1
  while True:
    if s[index] == -1 :
      break
    # 노드 번호, 노드까지의 거리 
    b, c = s[index], s[index+1]
    # 트리 추가 
    graph[s[0]].append((b,c))
    graph[b].append((s[0],c))
    index += 2 
    
# 1번 노드에서 다른 노드까지의 거리 구하기
dist = dijkstra(1)
# 가장 거리가 긴 노드의 번호 
tmp = dist.index(max(dist))
# 해당 노드에서 다른 노드까지의 거리 중 가장 긴 거리 출력 
print(max(dijkstra(tmp+1)))
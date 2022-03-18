# https://www.acmicpc.net/problem/11779
import sys, heapq 
input = sys.stdin.readline 
n = int(input())
m = int(input())

INF = int(1e9)

graph = [ [] for _ in range(n+1) ]

# 최단 거리저장 
distance = [INF] * (n+1)
# 경로 저장 
path = [ [] for _ in range(n+1) ]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
start,end = map(int,input().split())

def dijkstra(start):
    q = []
    distance[start] = 0 
    heapq.heappush(q, (0,start))
    path[start].append(start)
    
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 경우 
        if distance[now] < dist :
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            # 갱신 
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q,(cost,i[0]))
                # path 갱신 : now까지의 경로 + 현재 위치 
                path[i[0]] = []
                for p in path[now]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])
                
dijkstra(start)
print(distance[end])
print(len(path[end]))
print(*path[end])
# https://www.acmicpc.net/problem/1956
import heapq 
import sys
input = sys.stdin.readline 

INF = int(1e9)

v, e = map(int,input().split())    

graph = [ [] for _ in range(v+1) ]
# distance[i][j] 는 i에서 j로 가는 최단 거리 
distance= [ [INF] * (v+1) for _ in range(v+1) ]
q = []
    
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    distance[a][b] = c
    # 가능한 경로 
    heapq.heappush(q, (c,a,b))
    
while q :
    dist, a, b = heapq.heappop(q)
    # 출발지와 도착지가 같다면 사이클 발생 
    if a == b :
        print(dist)
        break
    
    # 이미 처리 됐다면 넘어감 
    if distance[a][b] < dist:
        continue

    # g에서 갈 수 있는 경로 
    for i in graph[b]:  
        cost = dist + i[1]
        
        # s -> g -> i[0] 보다 s -> i[0]이 빠르면 갱신 
        if cost < distance[a][i[0]] :
            distance[a][i[0]] = cost 
            heapq.heappush(q, (cost, a, i[0]))

else:
    print(-1)
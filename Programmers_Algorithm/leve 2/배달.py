# https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq
INF = int(1e9)

def solution(N, road, K):
    graph = [ [] for i in range(N+1)]
    distance = [INF] * (N+1)
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
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
    return sum(i <= K for i in distance)


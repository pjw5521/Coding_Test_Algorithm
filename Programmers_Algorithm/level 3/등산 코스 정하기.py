# https://school.programmers.co.kr/learn/courses/30/lessons/118669
import heapq 

def dijkstra(n, graph, gates, summits ):
    heap = []
    
    # intensity가 같다면, 산봉우리의 번호가 가장 낮아야 하므로 
    summits.sort()
    # intensity 저장 
    distance = [int(1e9)] * (n+1)
	
    # 출입구 힙에 넣어주기 
    for g in gates:
        distance[g] = 0 
        heapq.heappush(heap, (0, g))

    while heap :
        dist, now = heapq.heappop(heap)
		
        # 이미 더 짧은 intensity를 지나왔거나, 산봉우리에 도착했으면 
        if distance[now] < dist or now in summits :
            continue 
    	
        for i in graph[now]:
        	# intensity 구하기 
            cost = max(i[1], dist)
			
            # intensity 갱신 
            if cost < distance[i[0]] : 
                distance[i[0]] = cost 
                heapq.heappush(heap, (cost, i[0]))
	
    result = int(1e9)   
    num = 0 
    # intensity가 가장 작은 등산 코스 구하기 
    for s in summits:  
        if distance[s] < result :
            result = distance[s]
            num = s 

    return [num, result]

def solution(n, paths, gates, summits):
    graph = [ [] for _ in range(n+1)]

    for a,b,c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))

    return dijkstra(n, graph, gates, summits)
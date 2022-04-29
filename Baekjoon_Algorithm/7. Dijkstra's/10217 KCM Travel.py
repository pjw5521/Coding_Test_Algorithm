# https://www.acmicpc.net/problem/10217
t = int(input())
INF = int(1e9)

for _ in range(t):
    n, m, k = map(int,input().split())
    
    graph = [ [] for _ in range(n+1) ]
    # 1번 도시에서 i번 도시까지 j 비용으로 갔을 때 최단 시간  
    knapsack = [ [INF] * (m+1) for _ in range(n+1)]
    # 1번 도시 최단 시간 초기화 
    knapsack[1][0] = 0
    
    for _ in range(k):
        u, v, c, d = map(int,input().split())
        graph[u].append((v,c,d))
        
    # 모든 비용에 대해서 
    for cost in range(m+1):
    	# 각 도시마다 
        for city in range(1,n+1):
        	# 해당 비용으로 이동할 수 있으면 
            if knapsack[city][cost] != INF :
            	# 인접 도시 최단 시간 갱신 
                for ad_city, c, d in graph[city]:
                	# 이동시간 
                    cal_d = knapsack[city][cost] + d 
                    # 이동 비용 
                    cal_c = cost + c 
                    
                    # 이동 비용이 m 이하이고 더 짧은 시간으로 갈 수 있다면 갱신 
                    if cal_c <= m and cal_d < knapsack[ad_city][cal_c] :
                        knapsack[ad_city][cal_c] = cal_d
                        
    
    # n번 도시까지 가는 최단 시간 구하기 
    result = min(knapsack[n])
    
    # 갈 수 없다면 
    if result == INF:
        print('Poor KCM')
    else:
        print(result)
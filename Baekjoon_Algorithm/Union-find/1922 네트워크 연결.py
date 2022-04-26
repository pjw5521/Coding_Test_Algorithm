# https://www.acmicpc.net/problem/1922
import sys
input = sys.stdin.readline 

n = int(input())
m = int(input())

graph = []

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append([a,b,c])

# 비용 기준으로 정렬
graph.sort(key = lambda x : x[2])

# 첫번째 섬 연결 정보 connect에 추가, 중복 제거를 위해 set 
connect = set([graph[0][0], graph[0][1]])
# 첫 가중치 
answer = graph[0][2]

while len(connect) < n :
	# 사이클을 형성하지 않는 간선 선택 
    for cost in graph:
    	# 다음 섬의 출발지와 목적지가 모두 connect에 있으면 넘어감 
        if cost[0] in connect and cost[1] in connect :
            continue 
        # 하나민 있는 경우 추가한 후 answer에 더하기 
        if cost[0] in connect or cost[1] in connect :
            connect.update([cost[0], cost[1]])
            answer += cost[2]
            break 
        
print(answer)
# https://www.acmicpc.net/problem/2098
import sys

input = sys.stdin.readline 

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
    
# n개의 비트를 모두 켠다는 의미 
VISITED_ALL = (1<<n)-1 
# n번 -> visited에서 방문하지 않은 도시 -> 0번 도시(시작도시) 경로 
cache = [[None] * (1<<n) for _ in range(n)]
INF = float('inf')
index = 1 

def find_path(last, visited):
	# 모든 경로를 다 돌았을 때 -> 즉 출발 위치를 0으로 정했으므로 현재 위치에서 0 으로 갈 때 
    if visited == VISITED_ALL :
    	# 경로가 존재하면 경로 리턴, 아니면 INF
        return graph[last][0] or INF
    
    # 이미 수행되었다는 뜻 
    if cache[last][visited] is not None:
        return cache[last][visited]
        
    tmp = INF
    for c in range(n):
    	# 다음 도시로 가능 비용이 존재하고, 해당 도시를 방문하지 않았으면 
        if visited & (1<<c) == 0 and graph[last][c] != 0:
        	# 최솟값 갱신 
            tmp = min(tmp, find_path(c, visited | (1<<c)) + graph[last][c])
    
    cache[last][visited] = tmp
    return tmp

# 임의의 출발 도시 0에서 시작 
print(find_path(0, 1<<0))
# 대표 문제 : 백준 11657번 타임머신 
# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline 

def bf(start):
    # 자기 자신까지의 거리 0 으로 초기화
    dist[start] = 0 
    # 정점 수 만큼 반복 
    for i in range(n):
        # 매 반복마다 모든 간선 확인 
        for j in range(m):
            # 현재 노드 
            node = edges[j][0]
            # 다음 노드 
            next_node = edges[j][1]
            # 가중치
            cost = edges[j][2]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧을 경우 
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                # 갱신
                dist[next_node] = dist[node] + cost
                # n-1 번 이후 반복에도 값이 갱신된다면 음수 순환 존재 
                if i == n-1:
                    return True
    return False 
    
n, m = map(int,input().split())
INF  = int(1e9)
# 간선에 대한 모든 정보 
edges = []
# 최단 거리 저장 
dist = [INF] * (n+1)

# 간선에 대한 정보 저장 
for _ in range(m):
    u, v, w = map(int,input().split())
    edges.append((u,v,w))

negative_cycle = bf(1)
# 음수 순환 존재 
if negative_cycle :
    print(-1)
else :
    for i in range(2,n+1):
        # 도달할 수 없는 경우 
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
            
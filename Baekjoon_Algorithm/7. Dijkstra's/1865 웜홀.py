# https://www.acmicpc.net/problem/1865
import sys
input = sys.stdin.readline 

def bf(start):
    dist = [INF] * (n+1)
    # 자기 자신까지의 거리 0 으로 초기화
    dist[start] = 0 
    for i in range(n):
        # 매 반복마다 모든 간선 확인 
        for edge in edges:
            # 현재 노드 
            node = edge[0]
            # 다음 노드 
            next_node = edge[1]
            # 가중치
            cost = edge[2]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧을 경우 
            if dist[next_node] > dist[node] + cost:
                # 갱신
                dist[next_node] = dist[node] + cost
                # n-1 번 이후 반복에도 값이 갱신된다면 음수 순환 존재 
                if i == n-1:
                    return True
    return False 
    
test = int(input())
INF = int(1e9)
for _ in range(test):
    n, m, w = map(int,input().split())
    
    edges = []

    for _ in range(m):
        a, b, c = map(int,input().split())
        edges.append((a,b,c))
        edges.append((b,a,c))
        
    for _ in range(w):
        a, b, c = map(int,input().split())
        edges.append((a,b,-c))
        
    cycle = bf(1)
    if cycle:
        print('YES')
    else:
        print('NO')
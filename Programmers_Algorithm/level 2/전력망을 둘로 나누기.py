# https://programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque 

def bfs(start,graph,visited):
    visited[start] = True
    # 연결된 노드의 개수 
    cnt = 1
    q = deque()
    q.append(start)
    
    while q :
        x = q.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                cnt += 1 
                visited[i] = True
                q.append(i)
                
    return cnt 
    
def solution(n, wires):
    answer = int(1e9)
    
    graph = [ [] for _ in range(n+1) ]  
    
    # 그래프 생성 
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    # 모든 연결선에 대하여 
    for a, b in wires:
        visited = [False] * (n+1)
        # 방문 표시를 통해 연결 끊기 
        visited[b] = True
        # bfs로 연결된 노드 개수 구하기 
        count1 = bfs(a,graph,visited)
        # 전체 개수에서 다른 트리 노드 개수 빼면 다른 트리의 노드 개수 
        count2 = n - count1

        # 차이의 최솟값 갱신 
        if answer > abs(count1-count2):
            answer = abs(count1-count2)
            
    return answer
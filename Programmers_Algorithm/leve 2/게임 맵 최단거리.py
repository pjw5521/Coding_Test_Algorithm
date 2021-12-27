#https://programmers.co.kr/learn/courses/30/lessons/1844
# bfs 사용 

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(maps):
    n = len(maps)
    m= len(maps[0])
    answer=bfs(maps,n,m,0,0)
    # 마지막 위치까지 거리가 변하지 않았으면 도착을 못했다는 뜻 
    if answer != 1 :
        return answer
    return -1

def bfs(graph, n, m, x,y):
    q = deque()
    
    q.append((x,y))
    
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if ( 0 <= nx < n) and (0 <= ny <m) and graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]
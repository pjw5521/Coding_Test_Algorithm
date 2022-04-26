# https://programmers.co.kr/learn/courses/30/lessons/67259﻿
from collections import deque 

# 아래, 위, 오른쪽, 왼쪽 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
INF = int(1e9)

def bfs(x,y,n,d, board):
    q = deque()
    
    # 위치, 방향, 비용 
    q.append((x,y,d,0))
    # 비용 저장할 테이블 
    cost = [[INF]*n for _ in range(n)]
    # 출발 위치 비용 초기화 
    cost[x][y] = 0 
    
    while q :
        x, y, d, c = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            new_cost = 0 
            # 직진 시 직진 도로 비용 100 
            if d == i :
                new_cost = c + 100
            # 커브 시 비용 직진 도로 100 + 코너 500 
            else:
                new_cost = c + 600
            
            # 범위에 속하고, 벽이 아니고, 더 최소비용으로 이동할 수 있을 때 
            if 0<= nx < n and 0 <= ny < n and board[nx][ny] != 1 and cost[nx][ny] >= new_cost:
                # 최소 비용 갱신 
                cost[nx][ny] = new_cost 
                # 큐에 추가 
                q.append((nx,ny,i,new_cost))
                    
    return cost[n-1][n-1]
    
def solution(board):
    result = 0 
    # 첫 출발점에서 아래로 이동했을 때와 오른쪽으로 이동했을 때 최솟값 
    result = min(bfs(0,0,len(board),0, board), bfs(0,0,len(board),2, board))
    
    return result
    
b = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(b))
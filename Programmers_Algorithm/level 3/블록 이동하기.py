# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def move(pos1, pos2, board):

    pos = []
    
    for i in range(4):
        n1 = (pos1[0] + dx[i], pos1[1] + dy[i])
        n2 = (pos2[0] + dx[i], pos2[1] + dy[i])
        
        # 상하좌우 이동 
        if board[n1[0]][n1[1]] == 0 and board[n2[0]][n2[1]] == 0 :
            pos.append((n1,n2))
        
    # 수평일 때 
    if pos1[0] == pos2[0]:
        for i in [-1,1]:
            if board[pos1[0] + i][pos1[1]] == 0 and board[pos2[0] +i][pos2[1]] == 0:
                pos.append((pos1, (pos1[0]+i, pos1[1])))
                pos.append((pos2, (pos2[0]+i, pos2[1])))
    else:
       for i in [-1,1]:
            if board[pos1[0]][pos1[1]+i] == 0 and board[pos2[0]][pos2[1]+i] == 0:
                pos.append(((pos1[0], pos1[1]+i), pos1))
                pos.append(((pos2[0], pos2[1]+i), pos2)) 
    
    return pos
    
def solution(board):
    answer = 0
    n = len(board)
    new_board = [ [1] * (n+2) for _ in range(n+2) ]
    
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    n = len(board)
    visited = set()
    visited.add((1,1))
    visited.add((1,2))
    q = deque()
    q.append(((1,1),(1,2), 0))
    
    while q :
        pos1, pos2, cnt = q.popleft()
        
        if pos1 == (n, n) or pos2 == (n,n):
            return cnt 
            
        for k in move(pos1, pos2, new_board):
            if k not in visited:
                q.append((*k, cnt +1))
                visited.add(k)
    
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    
    for i in range(1, len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] >= 1 :
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
    answer = 0 
    
    for i in board:
        answer = max(answer,max(i))
        
    return answer * answer
    
    
board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))
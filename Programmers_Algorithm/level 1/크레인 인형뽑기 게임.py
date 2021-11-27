#https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    result = []
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move-1] != 0:
                result.append(board[i][move-1])
                board[i][move-1] = 0 
                break
        if len(result) > 1 :
            if result[-1] == result[-2] :
                answer += 2
                result = result[:-2]
                
    return answer
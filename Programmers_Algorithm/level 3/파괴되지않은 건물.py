# https://school.programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    answer = 0 
    n = len(board)
    m = len(board[0])

    dp = [ [0] * (m+1) for _ in range(n+1)]

    # 누적합 표시  
    for type, r1, c1, r2, c2, degree in skill:
        if type == 2 :
            degree = -degree  
        dp[r1][c1] -= degree 
        dp[r1][c2+1] += degree 
        dp[r2+1][c1] += degree 
        dp[r2+1][c2+1] -= degree 
    
    # 가로 누적합 
    for i in range(n):
        for j in range(m):
            dp[i][j+1] += dp[i][j]
    
    # 세로 누적합
    for i in range(n):
        for j in range(m):
            dp[i+1][j] += dp[i][j]

    # 기존 배열과 더하기     
    for i in range(n):
        for j in range(m):
            if board[i][j] + dp[i][j] > 0 :
                answer += 1 

    return answer
# https://www.acmicpc.net/problem/17070
import sys
input = sys.stdin.readline 

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 가로 : 0 , 세로 : 1, 대각선 : 2    
dp = [ [[0] * n for _ in range(n)] for _ in range(n) ] 

dp[0][0][1] = 1 
# 첫 줄는 가로로 오는 방법 밖에 없으므로 첫줄 초기화 
for i in range(2,n):
    if graph[0][i] == 0 :
        dp[0][0][i] = dp[0][0][i-1]

# 두번째 줄부터 
for i in range(1,n):
    # 파이프가 (1,1)와 (1,2)를 차지하고 있으므로 두번째 칸부터 가능 
    for j in range(2,n):
        # 현재 위치가 대각선일 때 
        if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
            # 가로에서 대각선으로 오는 방법 + 세로에서 대각선으로 오는 방법 + 대각선에서 대각선으로 오는 방법
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        # 현재 위치가 가로 또는 세로 일 때
        if graph[i][j] == 0:
            # 세로 일 때 = 세로에서 세로로 오는 방법 + 대각선에서 세로로 오는 방법
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
            # 가로 일 때 = 가로에서 가로로 오는 방법 + 대각선에서 가로로 오는 방법 
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            
answer = 0 
for i in range(3):
    answer += dp[i][n-1][n-1]
    
print(answer)
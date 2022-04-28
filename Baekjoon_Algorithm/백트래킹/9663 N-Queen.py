# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline 

def dfs(depth):
    global count 
    # n개 다 놓았으면 개수 증가 
    if depth == n:
        count += 1 
    else :
        for i in range(n):
            # 퀸 놓기 
            graph[depth] = i
            
            result = True
            # 위에 놓여있는 퀸들이랑 비교 
            for j in range(depth):
                # 같은 열에 위치하거나 대각선에 위치하면 놓을 수 없음 
                if graph[depth] == graph[j] or abs(graph[depth] - graph[j]) == depth-j:
                    result= False
                    break
                    
            # 놓을 수 있으면 
            if result :
                dfs(depth+1)
 
n = int(input())
count = 0   
# (인덱스 번호, 값)
graph = [0] * n
dfs(0)
print(count)
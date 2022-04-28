# https://programmers.co.kr/learn/courses/30/lessons/12952
cnt = 0 
def dfs(depth,n):
    global cnt, graph
    
    # 다 놓았으면 개수 증가 
    if depth == n :
        cnt += 1 
    else :
        for i in range(n):
            graph[depth] = i 
            
            result = True
            # 놓을 수 있는지 
            for j in range(depth):
                if graph[depth] == graph[j] or abs(graph[depth]- graph[j]) == abs(depth-j):
                    result = False 
                    break
            
            # 놓을 수 있으면 
            if result :
                dfs(depth+1,n)
                
def solution(n):
    global graph, cnt 
    
    graph = [0] * n 
    
    dfs(0,n)
    return cnt 
    
n =4 
print(solution(n))
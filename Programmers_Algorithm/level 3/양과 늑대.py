# https://school.programmers.co.kr/learn/courses/30/lessons/92343
answer = 0

def dfs(sheep, wolf, edges, visited, info):
    global answer 

    if sheep > wolf :
        answer = max(answer, sheep)
    # 늑대의 수가 양의 수보다 같거나 크면 탐색 종료 
    else :
        return 
	
    # 부모노드, 자식 노드 
    for p, c in edges:
    	# 부모노드는 방문했고, 자식 노드는 방문하지 않았으면 
        if visited[p] and not visited[c]:
            visited[c] = True 
            # 양이면 
            if info[c] == 0 :
                dfs(sheep+1, wolf ,edges, visited, info)
            # 늑대이면 
            else :
                dfs(sheep, wolf + 1, edges, visited, info)
            visited[c] = False 

def solution(info, edges):
    
    global answer 

    visited = [False] * len(info)
    visited[0] = True 
    # 루트는 무조건 양이므로 
    dfs(1, 0, edges ,visited, info) 

    return answer
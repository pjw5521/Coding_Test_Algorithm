# https://programmers.co.kr/learn/courses/30/lessons/17679
import copy 

def remove(graph, m, n):
    # 제거된 블록개수 
    pops = 0
    
    # 제거된 블록 수 체크할 배열 
    tmp =  copy.deepcopy(graph)
    
    for i in range(1,n):
        for j in range(1,m):
            # 블록이 없는 곳이면 넘어가기  
            if graph[i][j] == -1:
                continue 
            # 사라질 수 있으면 
            if graph[i][j] == graph[i-1][j] == graph[i][j-1] == graph[i-1][j-1]:
                # 0으로 채워넣기 
                tmp[i][j], tmp[i-1][j], tmp[i][j-1], tmp[i-1][j-1] = 0,0,0,0
    
    for i, v in enumerate(tmp):
        # 0 의 개수세기 
        cnt = v.count(0)
        pops += cnt 
        # 위에 있던 블록들 떨어뜨려주기 
        tmp[i] = [-1] * cnt + [ a for a in v if a!= 0] 
                
    return tmp, pops 
    
def solution(m, n, board):
    answer = 0 
    # 행과 열 뒤집기 
    graph = list(map(list, zip(*board)))

    while True:
        graph, pops = remove(graph,m,n)
        # 더이상 제거될 블록이 없으면 
        if pops == 0 :
            return answer 
        # 제거된 블록 수 더하기 
        answer += pops 

m = 4
n = 5
b = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,b))
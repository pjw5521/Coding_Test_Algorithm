# https://programmers.co.kr/learn/courses/30/lessons/87377
def solution(line):
    answer = []
    # 교점의 좌표 저장할 배열 
    result = []
    graph = [] 
    INF = float('inf')
    # 최소한의 크기만 나타내야 하므로 x,y 좌표의 최대, 최소 저장할 변수 
    min_x = INF
    min_y = INF
    max_x = -INF
    max_y = -INF
    
    # 직선 간의 교점 구하기 
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = map(int,line[i])
            c, d, f = map(int,line[j])
            
            # 분모가 0이 아니면 
            if (a*d - b*c) != 0 :
            	# x, y 좌표 구하기 
                x = (b*f - e*d) / (a*d - b*c)
                y = (e*c - a*f) / (a*d - b*c)
                # 둘 다 정수이면 
                if int(x) == x and int(y) == y:
                	# 이미 존재하는 교점이 아니면 
                    if (x,y) not in result :
                        x = int(x)
                        y = int(y)
                        # 배열에 저장 
                        result.append((x,y))
                        # x,y 좌표의 최대, 최소 구하기 
                        max_x = max(max_x, x)
                        min_x = min(min_x, x)
                        min_y = min(min_y, y)
                        max_y = max(max_y, y)

 	# "."으로 이루어진 그래프 만들기 
    graph = [ ['.'] * (abs(max_x-min_x)+1) for _ in range(abs(max_y-min_y)+1)]
    
    # 별 찍기 
    for x,y in result :
        a = abs(max_y - y) 
        b= abs(min_x - x)
        graph[a][b] = '*'
        
    for i in graph:
        answer.append("".join(i))
    return answer

line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line))
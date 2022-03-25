# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    
    data = [ [0] * columns for _ in range(rows)]
    num = 1 
    
    # 배열 생성 
    for a in range(rows):
        for b in range(columns):
            data[a][b] = num
            num += 1 

    for x1, y1, x2, y2 in queries:
        # 가장 왼쪽 위에 속하는 숫자 
        tmp = data[x1-1][y1-1]
        # 최솟값 저장할 변수 
        min_num = tmp
        
        # 왼쪽 세로 줄 이동 
        for i in range(x1-1, x2-1):
            t = data[i+1][y1-1]
            data[i][y1-1] = t 
            print(t)
            min_num = min(min_num,t)
            
        # 위쪽 가로 줄 이동 
        for i in range(y1-1, y2-1):
            t = data[x2-1][i+1]
            data[x2-1][i] = t
            min_num = min(min_num,t)
            
        # 오른쪽 가로 줄 이동 
        for i in range(x2-1,x1-1,-1):
            t = data[i-1][y2-1]
            data[i][y2-1] = t
            min_num = min(min_num,t)
    
        # 아래쪽 가로 줄 이동 
        for i in range(y2-1, y1-1,-1):
            t = data[x1-1][i-1]
            data[x1-1][i] = t
            min_num = min(min_num,t)
        
        # 가장 왼쪽 위 숫자 오른쪽으로 한칸 이동 
        data[x1-1][y1] = tmp
        # 최솟값 저장 
        answer.append(min_num)
            
    return answer

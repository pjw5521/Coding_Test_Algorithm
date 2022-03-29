# https://programmers.co.kr/learn/courses/30/lessons/68936
answer = [0] * 2 

def sol(arr, x,y,n):
    global answer
    
    # 시작 숫자 
    start = arr[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            # 다른 숫자 존재하면 분할 
            if arr[i][j] != start :
                sol(arr,x, y, n//2)
                sol(arr,x+n//2 , y , n//2)
                sol(arr,x, y+n//2, n//2)
                sol(arr,x+n//2, y + n//2, n//2)
                return 
    
    # 1로 압축 가능하면 
    if start == 1 :
        answer[1] += 1
    # 0으로 압축 가능하면 
    else:
        answer[0] += 1
            
def solution(arr):
    global answer
    sol(arr,0,0,len(arr))
    
    return answer
    
arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
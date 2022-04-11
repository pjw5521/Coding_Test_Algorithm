# https://programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 1
    
    for i in range(1,n+1):
        s = i 
        for j in range(i+1, n+1):
            if s == n :
                answer += 1 
            s += j 
            if s > n :
                break 
            
    return answer
    
n = 6
print(solution(n))
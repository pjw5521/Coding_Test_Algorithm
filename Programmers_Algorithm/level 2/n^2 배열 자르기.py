# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    
    for i in range(int(left),int(right)+1):
        # 몫 
        a = i // n
        # 나머지
        b = i % n 
        # 둘 중 더 큰 값 + 1 
        if a > b :
            answer.append(a+1)
        else:
            answer.append(b+1)
            
    return answer
    
n = 3
l = 2
r = 5
print(solution(n,l,r))
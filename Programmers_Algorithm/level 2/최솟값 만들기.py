# https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0

    # 오름차순 정렬
    A.sort()
    # 내림차순 정렬 
    B.sort(reverse = True)
    
    for x,y in zip(A,B):
        answer += x * y
        
    return answer
    
a = [1, 2]
b= [3, 4]
print(solution(a,b))
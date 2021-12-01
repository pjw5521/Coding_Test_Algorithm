#https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    result =0
    for i in d:
        num = result + i
        if num > budget :
            break
        else:
            result = num
            answer += 1 
    
    return answer
#https://programmers.co.kr/learn/courses/30/lessons/42889#
# 프로그래머스와 replit에서 같은 코드 실행 값이 다름 ... 

def solution(N, stages):
    answer = []
    dic = {}
    num = len(stages)
    
    for i in range(1, N+1):
        if num != 0:
            count = stages.count(i)
            dic[i] = count / num
            num -= count
        else:
            dic[i] = 0
            
    return sorted(dic, key = lambda x: dic[x], reverse= True)
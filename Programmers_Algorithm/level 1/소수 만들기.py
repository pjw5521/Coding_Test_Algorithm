#https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations
def solution(nums):
    answer = 0
    
    combine = list(combinations(nums,3))
    
    for i in combine:
        result = sum(i)
        b = False
        for i in range(2,result):
            if result % i == 0:
                b = True
                
        if b == False :
            answer += 1 
        
    return answer
# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations 
from collections import Counter 

def solution(orders, course):
    answer = []
    
    for num in course : # 요리의 개수별로 
        data = []
        
        for order in orders:
            combine = combinations(sorted(order), num) # 주문 별 가능한 음식 조합 구하기
            data += combine 
            
        count = Counter(data) # 음식 조합 별 중복 개수 구하기
        
        if count :
            max_num = max(list(count.values())) # 중복 개수 최댓값 구하기
            if max_num >= 2 : # 최댓값이 2 이상이면 
                for key, value in count.items(): 
                    if value == max_num:
                        answer.append("".join(key)) # 문자 연결
        
    return sorted(answer) # 코스별 메뉴 구성 정렬
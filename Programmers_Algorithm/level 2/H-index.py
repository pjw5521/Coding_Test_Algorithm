#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):  
    # 정렬 
    citations.sort()
    
    for index, c in enumerate(citations):
        # h번 이상 인용된 논문이 h편 이상 
        if c >= len(citations) - index :
            return len(citations) - index 
    return 0

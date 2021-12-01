#https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    start = left 
    if start == 1:
        answer -= 1 
        start += 1 
    while start <= right:
        count = 0 
        for i in range(2, start):
            if start % i == 0:
                count += 1
        if count % 2 == 0:
            answer += start 
        else:
            answer -= start 
        start += 1
        
    return answer
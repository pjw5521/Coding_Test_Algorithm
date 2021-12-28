#https://programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque

def solution(s):
    answer = True
    q = deque(s)
    count = 0
    while q :
        x = q.popleft()
        # ( 이면 +1 
        if x == '(':
            count += 1
        # ) 이면 -1
        else :
            count -= 1
        # )가 ( 보다 많으면 올바르지 않은 괄호 
        if count < 0:
            answer = False 
            break
    # (와 )의 개수가 맞지 않으면 올바르지 않은 괄호       
    if count != 0:
        answer = False 
        
    return answer
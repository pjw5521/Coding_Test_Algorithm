#https://programmers.co.kr/learn/courses/30/lessons/76502
'''
틀린 코드 
from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)
    for _ in range(len(s)):
        result = check(queue)
        if result :
            answer +=1
        tmp = queue.popleft()
        queue.append(tmp)
        
    return answer

def check(s):
    count = 0 
    for i in s:
        if i == '[' or i =='{' or i =='(':
            count += 1 
        else : count -= 1
        if count < 0:
            return False
        
    return True
'''

from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)
    for _ in range(len(s)):
        result = check(queue)
        if result :
            answer +=1
        tmp = queue.popleft()
        queue.append(tmp)
        
    return answer

def check(s):
    count = 0 
    stack = []
    for i in s:
        if i == '[' or i =='{' or i =='(':
            stack.append(i)
        else:
            if not stack:
                return False
            x = stack.pop()
            if i ==')' and x != '(':
                return False 
            if i =='}' and x != '{':
                return False 
            if i ==']' and x != '[':
                return False 
    if not stack :
        return True
    return False
        
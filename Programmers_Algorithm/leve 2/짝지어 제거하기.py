# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    
    for i in range(len(s)):
        if not stack : 
            stack.append(s[i])  # 스택에 아무것도 없으면 추가 
        else :
            if s[i] == stack[-1]: # 스택 마지막과 같으면 스택에서 제거 
                stack.pop()
            else : stack.append(s[i]) # 다르면 스택에 추가 
    if stack : # 스택에 남아있으면 
        return 0
    else:
        return 1
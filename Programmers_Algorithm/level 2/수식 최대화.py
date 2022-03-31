# https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations

# 계산한 값 전달하는 함수 
def operate(num1,num2,o):
    if o == '+':
        return int(num1) + int(num2)
    if o == '-':
        return int(num1) - int(num2)
    if o == '*':
        return int(num1) * int(num2)
        
def calculate(exp, o):
    # 숫자와 연산자 배열에 넣기 
    array = []
    tmp = ""
    for i in exp :
        # 숫자면 숫자들 이어붙이기 
        if i.isdigit():
            tmp += i
        # 연산자면 숫자 배열에 추가, 연산자 배열에 추가 
        else :
            array.append(tmp)
            array.append(i)
            tmp = ""
    # 마지막 숫자 배열에 추가         
    array.append(tmp)
    
    for i in o:
        stack = []
        while len(array) > 0 :
            t = array.pop(0)
            # 현재 우선 순위가 가장 높은 연산자라면 계산
            if t == i:
                # stack에 추가된 가장 최근 숫자 + array에 담긴 연산자 다음의 숫자 + 연산자 
                stack.append(operate(stack.pop(), array.pop(0),t))
            # 숫자거나 현재 우선순위가 가장 높은 연산자가 아니라면 stack에 추가 
            else:
                stack.append(t)
        # array를 stack으로 갱신 
        array = stack 
    
    # 상금의 절댓값 
    return abs(int(array[0]))
        
def solution(expression):
    answer = 0
    
    # 우선 순위 경우의 수 구하기 
    permute = list(permutations(['+','-','*'],3))
    
    # 모든 우선 순위에 대하여 수식 값 구하고, 최댓값 구하기 
    for i in permute:
        answer = max(answer, calculate(expression, i))
        
    return answer
   
ex = "100-200*300-500+20"
print(solution(ex))
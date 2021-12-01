#https://programmers.co.kr/learn/courses/30/lessons/77484#fn1
def solution(lottos, win_nums):
    answer = []
    right = 0
    wrong = 0 
    for i in lottos:
        if i in win_nums:
            right += 1
        elif i not in win_nums and i != 0:
            wrong += 1 
    
    if len(lottos) - wrong != 0 :
        answer.append(7-(len(lottos)-wrong))
    else:
        answer.append(6)
        
    if right != 0:
        answer.append(7-right)
    else :
        answer.append(6)
    
    
    return answer
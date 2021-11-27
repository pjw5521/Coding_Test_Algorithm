#https://programmers.co.kr/learn/courses/30/lessons/42576
# 아래 코드 시간초과 
# 시간초과 시 dic 사용 고려 
'''
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i not in completion:
            answer = i
            break
        else:
            completion.remove(i)
            
    return answer
'''

def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        dic[i] = 0
        
    for i in participant:
        dic[i] += 1
        
    for i in completion:
        dic[i] -= 1
        
    for i in participant:
        if dic[i] > 0:
            return i
            
   
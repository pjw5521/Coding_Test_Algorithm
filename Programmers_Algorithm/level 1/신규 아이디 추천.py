# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for data in new_id:
        if data.isalpha() or data.isdigit() or data in {'-','_','.'}: 
            answer += data
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer[0] =='.' :
        answer = answer[1:] if len(answer)>1 else 'a'
        
    if answer[-1] =='.':
        answer = answer[:-1]
        
    if len(answer) == 0:
        answer += 'a' 
        
    if len(answer) >= 16:
        answer = answer[:15]
            
    if answer[-1] == '.':
        answer = answer[:-1]
    
    while len(answer) <3:
        answer += answer[-1]
        
    return answer
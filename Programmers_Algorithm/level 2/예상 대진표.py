# https://programmers.co.kr/learn/courses/30/lessons/12985
from collections import deque 

def solution(n,a,b):
	# 남은 참가자 
    q = deque([ i+1 for i in range(n)])
    # 라운드 번호
    cnt = 1
    # 현 라운드에서 붙을 총 팀의 개수 
    tmp = n // 2 
    # 현 라운드에서 남은 붙을 팀의 개수 
    num = tmp
    
    while q :
        # 두 참가자 빼기 
        x = q.popleft()
        y = q.popleft()
        
        # 현 라운드에서 남은 붙을 팀의 개수가 없으면 다음 라운드라는 뜻 
        if num == 0 :
            cnt += 1 
            num = tmp // 2
            tmp = tmp // 2  
            
        # 두 참가자가 a와 b이면 라운드 리턴 
        if x in (a,b) and y in (a,b) :
            return cnt 
        
        # 두 참가자 중 a가 있으면 이긴 사람 a 큐에 삽입 
        if x == a or y == a :
            q.append(a)
        # 두 참가자 중 b가 있으면 이긴 사람 b 큐에 삽입 
        elif x == b or y == b :
            q.append(b)
        # 두 참가자 모두 a와 b가 아니면 아무나 이겨도 상관없으므로 작은 값 삽입 
        else:
            q.append(min(x,y))
            
        # 현 라운드에서 남은 붙을 팀의 개수 줄이기 
        num -= 1
        
n = 16
a = 1
b = 16
print(solution(n,a,b))
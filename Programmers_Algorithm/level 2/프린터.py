# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    tmp = deque()
    
    # 첫번째 큐 : 요청이 들어온 순서대로 location과 중요도를 함께 저장 
    for i in range(len(priorities)):
      tmp.append((i, priorities[i]))
    
    # 중요도가 높은 순서대로 정렬 
    priorities.sort(reverse = True)
    
    # 두번째 큐 : 중요도가 높은 순서대로 저장 
    prior = deque(priorities)
    
    # 실행순서 저장
    count = 0 
    
    # 큐가 빌 때까지 
    while tmp:
    # 첫번째 큐의 맨 앞 요청의 중요도가 가장 높을 때 
      if tmp[0][1] == prior[0]:
      	#두 큐에서 제거 
        x = tmp.popleft()[0]
        prior.popleft()
      	# 실행순서 +1 
        count += 1
        # 실행된 요청이 요구한 location과 같다면 
        if x == location:
          break 
        # 중요도가 가장 높은 요청이 아니라면 회전 
      else:
        tmp.rotate(-1)

    return count

# any를 사용하여 수정한 코드 
from collections import deque

def solution(priorities, location):

    tmp = deque()
    
    for i in range(len(priorities)):
      tmp.append((i, priorities[i]))
    
    count = 0 
    
    while tmp:
    	# 더 큰 중요도가 존재한다면 
       if any(tmp[0][1] < q[1] for q in tmp):
         tmp.rotate(-1)
       else:
         x = tmp.popleft()[0]
         count +=1 
         if x == location:
           break

    return count
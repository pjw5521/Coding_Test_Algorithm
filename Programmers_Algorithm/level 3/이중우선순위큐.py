from collections import deque
def solution(operations):
    answer = []
    que = deque()
    for i in operations:
        # 첫 글자 I 이면 
        if i[0] == 'I':
        # 숫자 추가 
          que.append(int(i[2:]))
        # 큐가 비어있지 않고 
        elif que:
            # 최댓값 삭제 
          if i[0] == 'D' and int(i[2:]) == 1:
              que.remove(max(que))
            # 최솟값 삭제 
          else:
              que.remove(min(que))
          
    if que:
        # 최댓값, 최솟값 반환 
      answer = [max(que),min(que)]
    else:
        # 큐가 비어있으므로 
      answer = [0,0]
    
    return answer
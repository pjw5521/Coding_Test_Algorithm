#https://programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque 

def solution(people, limit):

  # people 을 오름차순 정렬해서 deque 에 넣는다 
  q = deque(sorted(people))
  # 보트 개수 
  answer = 0 
  
  while q:
    # 길이가 1이면 보트 개수 +1 을 하고 끝 
    if len(q) == 1 :
      answer += 1 
      break 
    
    # 가장 큰 무게와 가장 작은 무게의 합이 limit보다 작거나 같으면 
    # 가장 큰 무게와 가장 작은 무게가 한 보트에 탈 수 있다면 
    if q[0] + q[-1] <= limit:
    # 큐에서 둘 다 제거 
      q.pop()
      q.popleft()
    else:
    # 큰 무게만 제거 
      q.pop()
    # 보트 수 + 1
    answer += 1 
  
  return answer
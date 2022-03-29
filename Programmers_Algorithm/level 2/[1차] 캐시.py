# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

def solution(cacheSize, cities):
    answer = 0
        
    # 캐시 사이즈가 0일 때 
    if cacheSize == 0:
        return 5 * len(cities)
    
    q = deque()
    for i in cities:
    	# 모두 소문자로 변경 
        i = i.lower()
        # 큐에 존재한다면 
        if i in q :
        	# 삭제 후 다시 삽입 
            q.remove(i)
            q.append(i)
            # 실행 시간 + 1 
            answer += 1 
        # 큐에 존재하지 않는다면 
        else:
        	# 큐에 캐시 사이즈만큼 도시가 들어가 있다면 
            if len(q) == cacheSize :
            	# 가장 오래전에 삽입된 거 삭제 후 도시 삽입 
                q.popleft()
                q.append(i)
            # 큐에 도시가 더 들어갈 수 있다면 
            else:
                q.append(i)
            # 실행 시간 + 5 
            answer += 5
            
    return answer
    
c = 5
ci= ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(c,ci))
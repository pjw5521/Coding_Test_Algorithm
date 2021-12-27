#https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []
    day = deque()
    
    for i in range(len(progresses)):
        count = 0 
        while progresses[i] < 100 :
            progresses[i] += speeds[i]
            count += 1 
            
        day.append(count)
    print(day)
    result = 1
    
    while day:
        data = day.popleft()
        while day:
          test = day.popleft()
          if test <= data:
            result += 1
          else:
            day.appendleft(test)
            break
        answer.append(result)
        result = 1

    return answer
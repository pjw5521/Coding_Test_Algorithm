#https://programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    # 큐에 더하거나 뺀 결과와 index를 저장 
    queue.append((0,0))

    while queue:
        # 더한 결과와 index
      result, index = queue.popleft()
      # index가 주어진 숫자들의 개수와 같다면 마지막 숫자라는 뜻 
      if index == len(numbers):
          # 최종 결과과 target 숫자와 같은지 비교 
        if result == target:
            # 같다면 방법의 수 + 1 
          answer +=1 
      else :
        number = numbers[index]
        # 더하고 뺀 결과 저장, index + 1 
        queue.append((result + number, index + 1))
        queue.append((result - number, index +1 ))
    return answer


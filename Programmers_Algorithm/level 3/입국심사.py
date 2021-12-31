#https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    answer = 0
    left = 0 
    # 가장 긴 시간이 걸리는 심사관한테 n명이 모두 심사받는 경우가 가장 오래 걸리는 경우 
    right = max(times) * n
    # 이진 탐색 
    while left <= right:
      mid = (left+right) // 2 
      people = 0 

      for time in times:
        # 각 심사관 별 mid동안 심사할 수 있는 사람의 수 
        people += (mid // time)

        # 심사받아야할 사람 수보다 더 많은 사람을 심사할 수 있다면, 시간 줄이기 
        if people >= n:
          answer = mid 
          right = mid -1 
          break 
      
      # 심사받아야할 사람 수보다 적게 심사한다면, 시간 늘리기 
      if people < n :
        left = mid + 1 

    return answer
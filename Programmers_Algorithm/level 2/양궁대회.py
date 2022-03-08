# https://programmers.co.kr/learn/courses/30/lessons/92342
from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
  # 가장 큰 차이 
  max_result = 0
  # 가장 큰 차이가 날 때의 조합 
  max_combine = {}
  # 중복 조합 
  combine = list(combinations_with_replacement(range(11),n))
  
  for num in combine:
    cnt = Counter(num)
    # s1는 라이언 점수, s2는 어피치 점수 
    s1, s2 = 0,0
    for i in range(1,11):
      # 쏜 개수가 더 많으면 라이언 점수 더하기 
      if info[10-i] < cnt[i]:
        s1 += i 
      # 어피치가 더 많이 쐈으면 어피치 점수 더하기 
      elif info[10-i] > 0 :
        s2 += i 
    
    # 두 명의 점수차
    result = s1 - s2
    # 최대 점수차이면 갱신 
    if result > max_result:
      max_combine = cnt
      max_result = result 

  if max_result > 0:
    answer =[0] * 11
    for i in max_combine:
      answer[10-i] = max_combine[i]
    return answer 
  else:
    return [-1]
#https://programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict

def solution(clothes):
  answer = 1
  dic = defaultdict(int)
  for i in clothes:
    dic[i[1]] += 1 

  for i in dic.values():
    answer *= (i+1)
  
  return answer-1
# https://programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict 
import math 

def solution(fees, records):
  answer = []
  result = defaultdict(int)
  t_record = dict()

  for i in records:
    s = i.split()
    if s[2] == 'IN':
      h, m = map(int, s[0].split(":"))
      t_record[int(s[1])] = h*60 + m
    else :
      h, m = map(int, s[0].split(":"))
      result[int(s[1])] += (h*60 + m)- t_record.pop(int(s[1]))

  for i in t_record.keys():
    result[i] += (23*60 + 59) - t_record[i]
  
  
  result = sorted(result.items(), key = lambda x : x[0])

  for i in result:
    if i[1] <= fees[0]:
      answer.append(fees[1])
    else:
      answer.append(fees[1] + (math.ceil((i[1]-fees[0])/fees[2])) * fees[3])
  
  return answer


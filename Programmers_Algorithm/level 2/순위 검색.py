# https://programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations 
from collections import defaultdict

def solution(info, query):
  answer = []
  dic = defaultdict(list)
  
  for i in range(len(info)):
    s = info[i].split()
    conditions = s[:-1]
    score = int(s[4])
    # 가능한 조합 만들어 주기 
    for n in range(5):
      combine = list(combinations(range(4),n))
      for c in combine :
        t_c = conditions.copy()
        for v in c :
          t_c[v] = '-'
        changed_t_c = '/'.join(t_c)
        dic[changed_t_c].append(score)

  # 점수 정렬 
  for i in dic:
    dic[i].sort()

  for i in range(len(query)):
    s = query[i].split(' and ')
    tmp = s[-1].split()
    limit = int(tmp[1])
    s[-1] = tmp[0]
    
    q = '/'.join(s)
    # 조건에 대한 key가 존재하면 
    if q in dic:
      # 점수 리스트 
      data = dic[q]

      if len(data) > 0 :
        start, end = 0, len(data)
        while start != end and start != len(data):
          if data[(start+end)//2] >= limit:
            end = (start + end )// 2 
          else:
            start = (start+end) // 2 + 1 
        answer.append(len(data)-start)
    # 조건을 만족시키는 경우가 없다는 뜻이므로 
    else:
      answer.append(0)
  
  return answer
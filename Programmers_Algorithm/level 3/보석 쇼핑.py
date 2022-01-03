#https://programmers.co.kr/learn/courses/30/lessons/67258
def solution(gems):
  answer = []
  # 서로 다른 보석의 개수 
  num = len(set(gems))
  dic = dict()
  start, end = 0, 0 
  sect = len(gems)+1 

  while end < len(gems):
    # 보석 개수 저장 
    if gems[end] not in dic:
      dic[gems[end]] = 1 
    else:
      dic[gems[end]] += 1 
    
    end += 1 

    # 경로에 보석이 다 있다면 
    if len(dic) == num:
      while start < end:
        # 뒤에 하나 더 있다는 뜻이므로 start +1 
        if dic[gems[start]] > 1 :
          dic[gems[start]] -= 1 
          start += 1
        # 지정한 구간보다 현재 구간이 짧다면 구간 갱신 
        elif end - start < sect:
          sect = end-start 
          answer = [start+1,end]
          break
        else:
          break

  print(start,end)
  return answer
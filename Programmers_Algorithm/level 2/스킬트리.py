# https://programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
  answer = 0
  
  for i in skill_trees:
    index = 0 
    for j in i :
      result = True
      if j in skill:
        if j == skill[index]:
          index +=1 
        else :
          result = False
          break
    
    if result :
      answer += 1
      
  return answer
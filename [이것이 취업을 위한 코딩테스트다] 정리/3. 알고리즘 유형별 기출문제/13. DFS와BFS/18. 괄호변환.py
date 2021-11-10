# 문제 346쪽
#https://programmers.co.kr/learn/courses/30/lessons/60058

def balance_index(p):
  count = 0 
  for i in range(len(p)):
    if p[i] =='(':
      count += 1
    else:
      count -=1 
    if count == 0 :
      return i

def check_proper(u):
  count = 0
  for i in u:
    if i == "(":
      count += 1 
    else:
      if count == 0:
        return False
      count -=1 
  return True

def solution(p):
    answer = ''
    if p =='':
      return answer
    index = balance_index(p)
    u =p[:index+1]
    v = p[index+1:]
    if check_proper(u):
      answer = u + solution(v)
    else:
      answer = '('
      answer += solution(v)
      answer += ")"
      u = list(u[1:-1])
      for i in range(len(u)):
        if u[i] == '(':
          u[i] = ')'
        else:
          u[i] = '('
      answer += "".join(u)
      
    return answer
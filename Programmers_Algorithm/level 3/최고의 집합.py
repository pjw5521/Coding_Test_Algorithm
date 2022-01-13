# https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
  answer = []

  if n > s : 
    return [-1]
  
  num = s // n
  
  for _ in range(n):
    answer.append(num)
  
  index = len(s) -1
  
  for i in range(s%n):
    answer[index] += 1
    index -= 1 
    
  return answer
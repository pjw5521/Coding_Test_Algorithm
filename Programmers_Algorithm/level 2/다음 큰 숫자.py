# https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
  answer = 0
  b = str(format(n, 'b')).count('1')

  for i in range(n+1, 1000000):
    
    if str(format(i, 'b')).count('1')== b:
      answer = i 
      break

  return answer



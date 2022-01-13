#https://programmers.co.kr/learn/courses/30/lessons/12914
# dp 문제 
# 점화식 : d[i] = d[i-1] + d[i-2]
def solution(n):
  
  if n == 1:
    return 1

  d = [0] * n 

  d[0] = 1
  d[1] = 2

  for i in range(2, n):
    d[i] = (d[i-1] + d[i-2]) % 1234567

  return d[n-1]
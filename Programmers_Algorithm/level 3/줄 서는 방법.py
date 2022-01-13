# https://programmers.co.kr/learn/courses/30/lessons/12936
'''
순열로 푸니 시간 초과 
from itertools import permutations 
def solution(n, k):
  permute = list(permutations(range(1,n+1),n))
  
  return permute[k-1]
'''

# 팩토리얼 이용 
import math

def solution(n, k):
  answer = []
  
  # 각 숫자들 
  num = [i for i in range(1,n+1)]
  # 배열은 0부터 시작하므로 -1 
  k = k - 1 

 # 숫자가 다 배열될때까지 반복 
  while n > 0 :
    # 맨 앞자리에 올 숫자의 인덱스 
    a = k // math.factorial(n-1)
    # 구한 인덱스에 해당하는 숫자 answer에 넣음 
    answer.append(num[a]) 
    # 배열된 숫자 제거 
    del num[a]
    
    # k 줄이기 
    k = k % math.factorial(n-1)
    n -= 1 

  return answer


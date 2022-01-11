#https://programmers.co.kr/learn/courses/30/lessons/12987
'''
순열로 모든 조합 다 체크했는데 당연히 시간초과 
from itertools import permutations 

def solution(A, B):
  n = len(A)
  answer = -1
  permute = list(permutations(B,n))
  
  for team in permute:
    result = 0 
    for a, b in zip(A,team):
      if a < b :
        result += 1
      
    answer = max(answer, result)
  
  return answer
'''

def solution(A, B):
  answer = 0
  # 내림차순으로 정렬
  A.sort(reverse= True)
  B.sort(reverse = True)
  # 최댓값부터 비교 
  for a in A:
    # a의 값이 B의 최댓값보다 크면 이길 수 있는 수가 없다는 것이므로 다음 수로 넘어감 
    if a >= B[0]:
      continue
    # a의 값이 B의 최댓값보다 작으면 이길 수 있는 수가 있다는 것이므로 점수 +1, B의 최댓값 사용했으니 삭제 
    else:
      answer += 1 
      del B[0]

  return answer
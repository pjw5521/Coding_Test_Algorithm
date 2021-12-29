#https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations 
import math

def solution(numbers):

    # 연결된 숫자 자르기 
    tmp = list(numbers)

    answer = 0
    permute = []
    
    # 가능한 숫자 조합 구하기 (순서가 있으므로 순열 사용 )
    for i in range(1,len(numbers)+1):
      permute.extend(permutations(tmp,i))
    
    # 중복 제거를 위해 set 
    result = set()

    # 숫자 조합 합쳐서 하나의 숫자로 
    for i in permute:
      num = (''.join(i))
      result.add(int(num)) 
    
    # 1과 0이 아니면 소수인지 판별 
    for i in result:
      if i != 1 and i != 0 and is_prime_num(i):
        # 소수라면 개수 증가
        answer += 1
    return answer 
    
# 소수 판별 함수 
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True




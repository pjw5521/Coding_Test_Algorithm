# https://programmers.co.kr/learn/courses/30/lessons/77486
import math

def solution(enroll, referral, seller, amount):
  answer = []
  # 추천인 저장 
  dic = dict()
  # 이익 저장 
  result = dict()

  # 판매원 별 추천인과 이익을 0으로 설정 
  for i in range(len(enroll)):
    dic[enroll[i]] = referral[i] 
    result[enroll[i]] = 0 

  for i in range(len(seller)):
    # 판매량 저장 
    result[seller[i]] += amount[i]* 100
    # 판매한 사람 
    sel = seller[i]
    # 판매량 
    num = amount[i] * 100
    # 추천인들에게 분배 
    while True:
      # 현재 판매원의 추천인 
      tmp = dic[sel]
      # 소수점 버림 
      pay = math.trunc(num*0.1)
      if pay ==0:
        break
    # 추천인이 민호인 경우
      if tmp == '-':
        result[sel] -= pay
        break
      # 추천인에게 10% 주고, 판매원에게서 제외 
      result[tmp] += pay
      result[sel] -= pay
      # 다음 추천인에게 해당되는 판매량 갱신 
      num = pay
      # 판매원 갱신 
      sel = tmp

  # 판매량만 리스트 형태로 
  return list(result.values())
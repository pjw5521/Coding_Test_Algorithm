#https://programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
  answer = 0

  if len(sticker) == 1 :
      return sticker[0]

 # result[i]는 index i번째까지 sticker에서 얻을 수 있는 최댓값 
 
 # 첫번째 스티커 때는 경우 
 # 마지막 인덱스 검사하면 안됨 
  result = [ 0 for _ in range(len(sticker))]

  result[0] = sticker[0]
  result[1] = sticker[0]

  for i in range(2, len(sticker)-1):
    result[i] = max(result[i-1], result[i-2] + sticker[i])

  answer = max(result)

 # 첫번째 스티커를 안 때는 경우 
 # 마지막 인덱스까지 검사 
  result = [ 0 for _ in range(len(sticker))]

  result[0] = 0
  result[1] = sticker[1] 

  for i in range(2, len(sticker)):
    result[i] = max(result[i-1], result[i-2] + sticker[i])
    
  return max(answer,max(result))
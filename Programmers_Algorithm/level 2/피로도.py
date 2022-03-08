# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations 

def solution(k, dungeons):
  answer = 0
  permute = []
  # 가능한 모든 순열 permute에 저장 
  for i in range(len(dungeons)):
    permute.extend(list(permutations(dungeons,i+1)))

  for p in permute:
    # 남은 피로도 
    tmp = k 
    # 탐험한 던전 후 
    cnt = 0
    for i in p:
      # 최소 필요 피로도를 만족시키면 탐험 
      if tmp >= i[0]:
        tmp -= i[1]
        cnt += 1 
    # 최대 던전 수가 크면 갱신 
    if cnt > answer :
      answer = cnt 
      # 답이 이미 최댓값이면 실행 중단 
      if answer == len(dungeons):
        break

  return answer
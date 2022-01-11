#https://programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
  answer = 0 
  # stations의 인덱스 
  idx = 0
  # 기지국 설치 위치 
  locate = 1
  
  while locate <=n :
  	# 전파 거리에 속하지 않거나, stations의 인덱스를 초과하였을 경우 
    if idx >= len(stations) or locate < stations[idx] - w :
      locate += w*2 + 1 
      answer += 1 
    # 전파 거리에 속할 때 
    else:
      locate = stations[idx] + w + 1
      idx += 1 

  return answer
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
  # 다리 
  q = [0] * bridge_length
  answer = 0 

  while q:
    # 시간 +1 
    answer += 1 
    
    # 다리 건넘 
    q.pop(0)

    if truck_weights:
      # 한계 무게를 넘지 않으면 
      if truck_weights[0] + sum(q) <= weight:
        # 다음 차도 다리에 올림 
        q.append(truck_weights.pop(0))
      else:
        q.append(0)
    
  return answer
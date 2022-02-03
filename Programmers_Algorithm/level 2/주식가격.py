# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
  # 유지된 시간 
  answer = [0] * len(prices)

  for i in range(len(prices)):
    for j in range(i, len(prices)):
      # 같거나 증가했으면 +1 
      if prices[i] <= prices[j]:
        answer[i] += 1 
      # 떨어졌으면 종료 
      else:
        answer[i] +=1 
        break
    
  return answer
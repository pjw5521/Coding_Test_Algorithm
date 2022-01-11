#https://programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
# 이진 탐색 범위 최솟값 
  left = 1 
# 이진 탐색 범위 최댓값 
  right = max(stones)
  answer = 0

# 이진 탐색 
  while left <= right :
    # 사용할 수 없는 블록 수 
    block = 0 
    mid = (left + right) // 2 

    for stone in stones :
      if stone - mid <= 0 :
        block += 1
      else :
        block = 0 
# 사용할 수 없는 블록 수가 k개 이상이면 
      if block >= k :
        break
# k 보다 작으면 범위 올리기 
    if block < k :
      left = mid + 1
# k 이상이면 정답 갱신하고 범위 낮추기 
    else:
      answer = mid 
      right = mid - 1 
  return answer

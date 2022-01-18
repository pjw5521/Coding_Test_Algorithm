# https://programmers.co.kr/learn/courses/30/lessons/12927
# 최대힙 문제 
import heapq

def solution(n, works):
  answer = 0
  heap = []

  # 파이썬은 최소힙만 지원해주므로 부호를 변경하여 최대힙 구현 
  for num in works:
    heapq.heappush(heap,-num)

  # n이 0일 때까지 
  while n > 0:
    work = heapq.heappop(heap)
   
   # 작업량이 가장 많이 남은 일이 0이면 남은 작업 모두 0이라는 뜻이므로 break
    if work == 0 :
      break

    # 1만큼 작업 처리 
    work += 1
    # n 줄이기
    n -= 1

    heapq.heappush(heap,work)

  for i in heap:
    answer += i*i

  return answer
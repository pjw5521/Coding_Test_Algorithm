# https://www.acmicpc.net/problem/11279
import heapq
import sys
input = sys.stdin.readline 

n = int(input())

h = []
for _ in range(n):

  x = int(input())

  if x == 0:
    if h:
      # 절댓값 출력 
      print(abs(heapq.heappop(h)))
    else:
      print(0)
  else:   
    # 마이너스 부호 붙여서 삽입 
    heapq.heappush(h,-x)
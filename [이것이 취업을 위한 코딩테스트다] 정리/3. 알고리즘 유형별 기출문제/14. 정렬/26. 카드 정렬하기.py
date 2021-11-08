# 문제 363쪽
# https://www.acmicpc.net/problem/1715
# 우선 순위 큐 사용 
# 매번 가장 작은 거 두개 선택 

import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
  a = int(input())
  heapq.heappush(q, a)

result = 0 
while len(q) != 1:
  a = heapq.heappop(q)
  b = heapq.heappop(q)
  sum_value= a + b
  result += sum_value
  heapq.heappush(q, sum_value)

print(result)

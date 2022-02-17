# https://www.acmicpc.net/problem/7662
import heapq
import sys
input = sys.stdin.readline

# 동기화 
def sync(h):
  while h and not exist[h[0][1]]:
    heapq.heappop(h)
    
t = int(input())

for _ in range(t):
  n = int(input())
  
  max_heap = []
  min_heap = []
  # 인덱스는 입력된 숫자의 고유 번호 
  exist = [False] * 1000001
  
  for i in range(n):
    s, num = input().split()
    num = int(num)
    
    if s== 'I':
      heapq.heappush(max_heap, (-int(num), i))
      heapq.heappush(min_heap, (int(num), i))
      # 존재함을 표시 
      exist[i] = True
      
    if s == 'D':
      if num == -1 :
        sync(min_heap)
        
        if min_heap:
          exist[min_heap[0][1]] = False
          heapq.heappop(min_heap)
      else :
        sync(max_heap)
        
        if max_heap :
          exist[max_heap[0][1]] = False
          heapq.heappop(max_heap)

  sync(max_heap)
  sync(min_heap)
  
  if max_heap and min_heap:
    print(-max_heap[0][0], min_heap[0][0])
  else:
    print('EMPTY')
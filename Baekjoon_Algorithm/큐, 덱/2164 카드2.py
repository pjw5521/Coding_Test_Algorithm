# https://www.acmicpc.net/problem/18258

# 큐 사용하면 시간초과 

# 아래 코드 시간 초과 
'''
import sys
input= sys.stdin.readline
import queue

n = int(input())
q = queue.Queue()

for i in range(1, n+1):
  q.put(i)

while q.qsize() > 1:
  q.get()
  num = q.get()
  q.put(num)

print(q.get())
'''

# deque 사용 

import sys
input= sys.stdin.readline
from collections import deque

n = int(input())
q = deque()

for i in range(1, n+1):
  q.append(i)

while len(q) > 1:
  q.popleft()
  num = q.popleft()
  q.append(num)

print(q.pop())
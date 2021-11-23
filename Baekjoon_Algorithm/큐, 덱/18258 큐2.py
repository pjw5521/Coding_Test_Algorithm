# https://www.acmicpc.net/problem/18258
import sys
input= sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
  command = input().split()

  if command[0] == 'push':
    q.append(command[1])
  elif command[0] == 'pop':
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif command[0] == 'front':
    if q:
      num = q.popleft()
      print(num)
      q.appendleft(num)
    else:
      print(-1)
  elif command[0] == 'back':
    if q:
      num = q.pop()
      print(num)
      q.append(num)
    else:
      print(-1)
  elif command[0] == 'empty':
    if q:
      print(0)
    else:
      print(1)
  elif command[0] == 'size':
    print(len(q))
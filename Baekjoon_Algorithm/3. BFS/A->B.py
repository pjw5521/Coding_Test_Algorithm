#https://www.acmicpc.net/problem/16953
from collections import deque

a, b = map(int,input().split())

q = deque()

q.append((a, 1))

result = False

while q:
  num, index = q.popleft()

  if num == b:
    print(index)
    result = True
    break

  else:
    if num * 2 <= b :
      
      q.append((num*2, index +1))
    if int(str(num)+'1') <= b :
      q.append((int(str(num)+'1'), index+1))

if result == False:
  print(-1)


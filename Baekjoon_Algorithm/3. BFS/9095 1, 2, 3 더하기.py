# https://www.acmicpc.net/problem/9095
from collections import deque 

test = int(input())

for _ in range(test):
  
  n = int(input())
  
  if n == 1:
    print(1)
  elif n == 2:
    print(2)
  else:
    q = deque()
    
    for i in range(1,4):
      q.append(i)
    
    cnt = 0 
    while q:
      x = q.popleft()
      
      if x == n:
        cnt += 1 
      else:
        if x + 3 <= n:
          q.append(x+3)
        if x + 1 <= n:
          q.append(x+1)
        if x + 2 <= n:
          q.append(x+2) 

    print(cnt)
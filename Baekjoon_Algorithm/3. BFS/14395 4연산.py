# https://www.acmicpc.net/problem/14395
from collections import deque 

INF = int(10e9)

def bfs(s,t):

  check.add(s)

  q = deque()
  q.append((s,""))

  while q:
    num, result = q.popleft()
    
    # t와 같으면 결과 리턴 
    if num == t :
      return result 
      
    # 범위에 포함되고 방문한 적이 없으면 
    tmp = num*num
    if 0<= tmp <= INF and tmp not in check :
      q.append((tmp, result + "*"))
      check.add(tmp)
    
    tmp = num+num
    if 0<= tmp <= INF and tmp not in check :
      q.append((tmp, result + "+"))
      check.add(tmp)  
    
    # 나누기 연산하면 1이 됨 
    tmp = 1 
    if 1 not in check:
      q.append((tmp, result+"/"))
      check.add(1)

  return -1 

s, t = map(int,input().split())

# 방문 여부 확인 
check = set()

if s == t :
  print(0)
else :
  print(bfs(s,t))
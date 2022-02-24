# https://www.acmicpc.net/problem/16953
from collections import deque 

def bfs(a):
  q = deque()
  q.append((a,1))
  
  while q:
    x, cnt = q.popleft()

    if x == b:
      return cnt 

    if x*2 <= b :
      q.append((x*2, cnt + 1))
    
    # 스트링으로 바꿔 오른쪽에 '1'을 추가한 후 다시 int로 바꿔줌 
    tmp = int(str(x) + '1')
    if tmp <= b :
      q.append((tmp,cnt+1))

  return -1 

a, b = map(int,input().split())

print(bfs(a))
#문제 https://www.acmicpc.net/status?user_id=pjw5521&problem_id=1697&from_mine=1
# bfs로 최단거리 구하기
from collections import deque

def bfs():
  queue = deque()
  queue.append(n)
  while queue:
    x = queue.popleft()
    if x == k:
      print(dist[x]) # 도착위치면 도착위치까지의 거리 출력
      break
    for i in (x-1, x+1, x*2): # 가능한 이동 거리 
      if ( 0 <= i <= 10**5 ) and dist[i] == 0: # 배열의 최댓값을 벗어나지 않았고, 아직 안갔으면 
        dist[i] = dist[x] + 1
        queue.append(i)

dist = [0] * (10**5 + 1) # 거리 저장할 배열 
n, k = map(int,input().split())

bfs()
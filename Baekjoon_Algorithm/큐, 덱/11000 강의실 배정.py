# https://www.acmicpc.net/problem/11000
import heapq 

n = int(input())

q = []
for _ in range(n):
  a,b= map(int,input().split())
  q.append((a,b))

# 가장 시작 시간이 빠른 거부터 
q.sort()

answer = []

# 가장 시작 시간이 빠른 강의의 종료 시간 힙에 추가 
# 회의 종료 시간 기준으로 최소힙 구현 
heapq.heappush(answer,q[0][1])


for i in range(1,n):
  if q[i][0] < answer[0]:
    # 강의실 생성 
    heapq.heappush(answer,q[i][1])
  else:
    # 기존 강의실 삭제 후 종료 시간 갱신하여 다시 추가 
    heapq.heappop(answer)
    heapq.heappush(answer,q[i][1])

# 강의실의 개수 출력 
print(len(answer))
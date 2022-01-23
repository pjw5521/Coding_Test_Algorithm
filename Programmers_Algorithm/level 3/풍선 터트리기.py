# https://programmers.co.kr/learn/courses/30/lessons/68646
NF = int(1e9)

def solution(a):
  answer = 0 
  left , right = INF, INF

  # 각 숫자별 본인 왼쪽에 본인보다 제일 작은 수 
  # 각 숫자별 본인 오른쪽에 본인보다 제일 작은수 
  maps = [[ 0 for _ in range(len(a))] for _ in range(2)]

  # i 인덱스 왼쪽에 a[i]보다 가장 작은 수 
  for i in range(len(a)):
    if left > a[i]:
      left = a[i]

    maps[0][i] = left 
  
  # i 인덱스 오른쪽에 a[i]보다 가장 작은 수 
  for i in range(len(a)-1, -1, -1):
    if right > a[i]:
      right = a[i]
    
    maps[1][i] = right 
  
  for i in range(len(a)):
    # a[i] 기준 오른쪽이나 왼쪽의 최솟값보다 작거나 같을 경우 (가장 작은 수가 본인일 수도 있음)
    if a[i] <= maps[0][i] or a[i] <= maps[1][i]:
      answer += 1 

  return answer
#https://programmers.co.kr/learn/courses/30/lessons/42861
# 크루스칼 알고리즘(그리디 알고리즘)
def solution(n, costs):
  # cost 기준으로 오름차순 정렬 
  costs.sort(key = lambda x : x[2])
  # 첫번째 섬 연결 정보 connect에 추가. 중복 제거를 위해 set으로 설정 
  connect = set([costs[0][0],costs[0][1]])
  # 첫 가중치 
  answer = costs[0][2]
  
  while len(connect) < n:
    for cost in costs:
      # 다음 섬의 출발지와 목적지가 모두 connect에 존재하면 넘어감 
      if cost[0] in connect and cost[1] in connect:
        continue
      # 두 섬 중 하나만 connect에 있는 경우 추가한 후 answer에 가중치 더함 
      if cost[0] in connect or cost[1] in connect:
        connect.update([cost[0],cost[1]])
        answer += cost[2]
        break 

  return answer
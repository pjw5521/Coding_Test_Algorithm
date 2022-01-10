def solution(routes):
  answer = 1
  # 나가는 시간 기준으로 오름차순 정렬
  routes.sort(key = lambda x : x[1])
  # 처음 카메라 위치는 가장 먼저 차량이 나간 지점 
  camera = routes[0][1]

  for i in range(1, len(routes)):
    # 만약 다음 차량이 출발한 시점보다 카메라가 전에 있으면 
    if camera < routes[i][0]:
    # 카메라 개수 하나 증가 
      answer += 1
    # 카메라 위치 다음 차량이 나간 지점으로 이동 
      camera = routes[i][1]
      
  return answer
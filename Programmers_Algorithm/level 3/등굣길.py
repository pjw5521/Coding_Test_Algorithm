#https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    answer = 0
    # 거리를 저장할 지도 
    graph = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    # puddle 위치를 저장할 지도 
    puddels_arr = [ [0 for _ in range(m+1)] for _ in range(n+1)]
    
    # puddle 위치 표시 
    for a,b in puddles :
      puddels_arr[b][a] = 1 
    # 출발 지점 초기화 
    graph[1][1] = 1 

    for i in range(1,n+1):
      for j in range(1,m+1):
        # 출발 지점이면 넘어감 
        if i == 1 and j == 1 :
          continue 
        # 장애물이 있는 곳이면 넘어감 
        if puddels_arr[i][j] == 1:
          continue
        # 현재 위치까지의 거리는 = 왼쪽까지의 거리 + 위쪽까지의 거리 
        else : graph[i][j] = (graph[i-1][j] + graph[i][j-1]) % 1000000007 

    return graph[n][m]
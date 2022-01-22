# https://programmers.co.kr/learn/courses/30/lessons/17678
def solution(n, t, m, timetable):
  answer = 0
  
  # 크루 도착 시간 저장 
  crew_list = []
  # 버스 도착 시간 저장 
  bus_list = []
  
  # 크루 도착 시간 분으로 바꿔서 저장 
  for i in timetable:
    h_time, m_time = map(int,i.split(":"))
    crew_list.append(h_time*60 + m_time)

  # 먼저 도착한 크루 순으로 정렬 
  crew_list.sort()

  # 첫 버스 도착 시간 9 : 00 
  tmp = 9 * 60
  bus_list.append(tmp)

  # 버스 도착 시간 저장 
  for _ in range(n-1):
    tmp += t
    bus_list.append(tmp)

  # 탑승할 크루 인덱스 
  i = 0 
  
  # 버스 도착 시간마다 
  for bus_time in bus_list:
    # 해당 버스 도착 시 탑승한 크루 수 
    cnt = 0
	
    # 탑승한 크루 수보다 탑승할 수 있는 수가 많을 때
    # 탑승할 크루가 있을 때 
    # 탑승할 크루의 도착 시간이 버스 도착시간과 같거나 빠를 때 
    while cnt < m and i < len(crew_list) and crew_list[i] <= bus_time  :
      i += 1
      cnt += 1 
  
	# 버스에 탑승할 자리가 남아있으면, 버스 도착한 시간에 도착하면 됨 
    if cnt < m : 
      answer = bus_time
	# 버스에 탑승할 자리가 없으면, 마지막으로 탑승한 크루의 도착시간보다 1분 일찍 
    else :
       answer = crew_list[i-1] - 1
       
  return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
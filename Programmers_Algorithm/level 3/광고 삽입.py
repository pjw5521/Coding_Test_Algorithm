#https://programmers.co.kr/learn/courses/30/lessons/72414
def solution(play_time, adv_time, logs):
  
  # 전체 시간, 광고 시간 초단위로 변경 
  play = time_compute(play_time)
  adv = time_compute(adv_time)

  # i 시각에서 시청중인 사람의 수 
  all_time = [0 for i in range(play+1)]

  # 로그 별 시작 시간, 종료 시간 초단위로 변경 
  # 시청중인 사람 수 표시 
  for l in logs:
    start, end = l.split("-")
    start = time_compute(start)
    end = time_compute(end)

    all_time[start] += 1 
    all_time[end] -= 1 

  # 구간 별 시청자 수 구하기
  for i in range(1, len(all_time)):
    all_time[i] = all_time[i-1] + all_time[i]

  # 누적 시청자 수 구하기 
  for i in range(1, len(all_time)):
    all_time[i] = all_time[i-1] + all_time[i]

  most_view = 0 
  max_time = 0 

  for i in range(adv -1 , play):
    if i >= adv :
      if most_view < all_time[i] - all_time[i -adv]:
        most_view = all_time[i] - all_time[i-adv]
        max_time = i - adv + 1 
    else:
      if most_view < all_time[i]:
        most_view = all_time[i]
        max_time = i - adv + 1 
  
  return time_change(max_time)

# string 형식으로 표시된 시간 초단위로 변경 
def time_compute(time):
  h, m, s = time.split(":")
  return int(h) * 3600 + int(m)* 60 + int(s)

# 초단위로 표시된 시각 string 형식으로 변경 
def time_change(time):
  h = time // 3600 
  h = '0' + str(h) if h < 10 else str(h)
  time = time % 3600
  m = time // 60
  m = '0' + str(m) if m < 10 else str(m)
  time = time % 60
  s = '0' + str(time) if time < 10 else str(time)

  return h + ":" + m  + ":" + s
# https://programmers.co.kr/learn/courses/30/lessons/81303
def solution(n, k, cmd):
  answer = ''

  # 이중 연결 리스트 
  # 표의 위치별 이전 표와 다음 표 기록 
  linked_list = { i : [i-1, i+1] for i in range(n)}
  
  # 현재 가리키고 있는 위치 
  cursor = k 
  
  # 삭제된 표 정보 기록할 리스트 
  delete = []
  
  # 삭제 여부 기록할 리스트 
  state = ["O"] * n

  # 명령마다 
  for i in cmd:
    
    if len(i) > 1 :
      # 명령어와 칸 구분 
      s, num = i.split()
      num = int(num)
      
      # 다음 칸으로 이동 
      if s == 'D':  
        # 입력된 칸 수만큼 
         for _ in range(num):
          cursor = linked_list[cursor][1]

     # 이전 칸으로 이동 
      elif s == 'U':
        # 입력된 칸 수 만큼 
        for _ in range(num):
          cursor = linked_list[cursor][0]
    
    else :
      # 삭제 명령
      if i == 'C':
        # 이전 칸, 다음 칸 위치 기록 
        prev, nex = linked_list[cursor]
        # 삭제된 표 정보 기록 
        delete.append((prev,cursor,nex))
        # 삭제 정보 갱신 
        state[cursor] = 'X'
        
        # 맨 마지막 칸이 삭제되었다면 
        if nex == n:
          # 커서 이전 칸으로 이동 
          cursor = linked_list[cursor][0]
        else:
          # 커서 다음 칸으로 이동 
          cursor = linked_list[cursor][1]

        # 맨 앞 칸이 삭제 되었다면 
        if prev == -1:
          # 다음 칸의 이전 칸 정보만 갱신 
          linked_list[nex][0] = prev
        # 맨 마지막 칸이 삭제 되었다면 
        elif nex == n :
          # 이전 칸의 다음 칸 정보만 갱신 
          linked_list[prev][1] = nex
       # 중간에 있는 칸이 삭제 되었다면 
        else:
          # 이전 칸과 다음 칸의 정보 갱신 
          linked_list[prev][1] = nex
          linked_list[nex][0] = prev

      # 복구 명령 
      else:
        # delete 리스트에서 최근에 기록된 정보 pop 
        prev, now, nex = delete.pop()
        # 삭제 여부 갱신
        state[now] = 'O'

        # 맨 처음 칸이었다면 
        if prev == -1:
          linked_list[nex][0] = now
        # 맨 마지막 칸이었다면 
        elif nex == n:
          linked_list[prev][1]= now
        else :
          linked_list[prev][1]= now
          linked_list[nex][0] = now

  for x in state:
    answer += x 

  return answer

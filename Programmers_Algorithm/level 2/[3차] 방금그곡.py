# https://programmers.co.kr/learn/courses/30/lessons/17683
def get_time(x, y):
    x = int(x[:2]) * 60 + int(x[3:])
    y = int(y[:2]) * 60 + int(y[3:])
    
    return y-x

# 악보의 음을 구분한 배열 구하는 함수 
def get_s(s):
    
    result = []
    for i in range(len(s)):
        if s[i] == '#':
            continue 
        
        # 마지막 음이 '#'이 아니면 삽입 
        if i == len(s)-1 :
            result.append(s[i])
        else :
        	# '#'와 함께 구성된 음이면 
            if s[i+1] == '#':
                result.append(s[i:i+2])
            else:
                result.append(s[i])
    return result
        
def solution(m, musicinfos):
	# 정답 제목과 재생 시간 
    answer = ''
    t_answer = 0
    
    for music in musicinfos :
    	# ','을 기준으로 나누어서 각 변수에 대입 
        start, end, name, info = map(str,music.split(','))
        # 재생 시간 구하기 
        t = get_time(start,end)
        
        # 음 구분한 배열 구하기 
        result = get_s(info)
        # 악보의 총 길이 
        l = len(result)
        
        # 재생된 악보 저장할 배열 
        s = []
       	# 재생 기간에 악보 전체가 재생될 수 있는 수만큼 전체 악보 삽입 
        for _ in range(t//l):   
            s.extend(result)
        
        # 나머지 악보 삽입 
        for i in range(t%l):
            s.append(result[i])
          
        # 기억한 멜로디의 재생 길이 구하기 
        m_l = len(get_s(m))
        
        # 재생된 총 악보에 기억한 멜로디가 존재하는지 확인 
        for i in range(len(s)- m_l+1):
            if m == "".join(s[i:i+m_l]):
            	# 총 재생기간이 긴 것으로 갱신 
                if t_answer < t:
                    answer= name
                    t_answer = t 
      
   	# 일치하는 것이 없다면 
    if len(answer) == 0 :
        return '(None)'     
        
    return answer

m = "CC#BCC#BCC#BCC#B"
info = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m,info))
# https://programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer = []
    # 체크할 단어 위치 
    index = 0 
    # 단어 key, value는 색인 번호 
    dic = {} 
    # 다음 색인 번호 
    cnt = 27
    
    # A부터 Z까지 사전에 등록 
    for i in range(65, 99):
        dic[chr(i)] = i - 64
    

    while index < len(msg) :
		# 압축할 색인 번호 
        num = dic[msg[index]]
        s = ''
        # 현재 알파벳의 인덱스 위치 
        t = index 
        
        # 마지막 한개 알파벳이라면 
        if index == len(msg) -1 :
            answer.append(num)
            break
        
        for i in range(t+1, len(msg)+1):
			
            # 사전에 없는 단어라면 
            if msg[t:i] not in dic :
                s = msg[t:i]
                # 그 전까지 단어는 사전에 있었다는 뜻이므로 제거 후, 다음 알파벳부터 비교 
                index = i -1
                break
            # 사전에 있는 최대 길이의 단어까지 색인 번호 갱신 
            else:
                num = dic[msg[t:i]]
            
            # 단어 끝까지 존재하는 색인번호가 존재한다면 중단 
            if i == len(msg):
                index = len(msg)
        
        # 색인 번호 등록 
        dic[s] = cnt 
        # 다음 등록할 색인 번호 + 1
        cnt += 1 
        # 압축할 색인 번호 추가 
        answer.append(num)

    return answer
    
m = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(m))

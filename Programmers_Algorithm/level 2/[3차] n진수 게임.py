# https://programmers.co.kr/learn/courses/30/lessons/17687
# 진법에 맞는 숫자로 변환해주는 함수 
def cal(n, q):
    rev_base = ''
    
    while n > 0 :
        n, mod = divmod(n,q)
        
        # 10-15를 문자로 표현하기 위해 
        if mod >= 10 :
        	# 'A'의 아스키 코드 65 
            rev_base += chr(55+mod)
        else:
            rev_base += str(mod)
            
    index = 0
    # 앞에 0 제거하기 위해 뒤에서부터 0이 아닌 숫자 등장 인덱스 저장 
    for i in range(len(rev_base)-1, -1, -1):
        if rev_base[i] != '0':
            index = i 
            break

    return rev_base[index::-1]
    
def solution(n, t, m, p):
    answer = ''
    
    # 현재 순서 
    seq = 1
    # 10진수 숫자
    num = 0
    # 구한 횟수 
    cnt = 0 
    
    while True :
   		# 0 이면 진법 바꿀 필요 x 
        if num == 0:
            if seq == p :
                answer += '0'
                # 구한 횟수 +1 
                cnt += 1 
                if cnt == t :
                    return answer 
            # 순서 + 1
            seq += 1 
        else :    
        	# 진법 변환 
            c_num = cal(num, n)
			
            # 변환한 숫자의 길이만큼 
            for i in range(len(c_num)):
                # 순서 갱신 
                if seq > m :
                    seq = 1 
                
                # 튜브 차례
                if seq == p:
                    answer += c_num[i]
                    # 구한 횟수 + 1 
                    cnt += 1 
                    if cnt == t :
                        return answer 
            	#순서 + 1 
                seq += 1 
                
        # 10진수 숫자 증가 
        num += 1 
n = 16
t = 16
m = 2
p = 1 
print(solution(n,t,m,p))

'''참고 풀이
# 재귀함수로 10진수 n진수로 바꾸기 
def convert(n, base):
    arr= '0123456789ABCDEF'
    # n을 base로 나눈 몫과 나머지 
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q,base) + arr[r]
           
def solution(n, t, m, p):
    answer = ''
    num = ''
    
    # n진수로 변환한 숫자 미리 저장 
    for i in range(m*t):
        num += str(convert(i,n))
    
    while len(answer)< t :
        # 해당 인덱스에 위치한 값 따로 가져오기 
        answer += num[p-1]
        p += m 
        
    return answer
'''
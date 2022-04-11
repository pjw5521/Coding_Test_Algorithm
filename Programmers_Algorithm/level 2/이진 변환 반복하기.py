# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):

    cnt = 0
    zero = 0
    

    while True :
        # 1이면 결과 값 리턴 
        if s == '1':
            return (cnt, zero)
        
        # 정수형 리스트로 변환 
        t = list(map(int, s))
            
        # 제거 될 0 의 개수 
        zero += t.count(0)
        
        # 1의 개수 이진수 변환 
        s = bin(t.count(1))
        # 앞에 0x 제거 
        s = str(s[2:])
        # 변환횟수 + 1 
        cnt += 1

s = "110010101001"	
print(solution(s))
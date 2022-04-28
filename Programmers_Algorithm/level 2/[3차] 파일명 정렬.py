# https://programmers.co.kr/learn/courses/30/lessons/17686
def solution(files):
    answer = []
    data = []
    for f in files :
 
        head, num, tail = '', '', ''
        index = len(f)-1
        
        # 숫자 등장 인덱스 구하기 
        for i in range(len(f)):
            if f[i].isdigit():
                index = i 
                break
                
        # 숫자 등장 전까지 head
        head = f[:index]
        num = f[index:]
        
        for i in range(len(num)):
        	# 문자 등장 인덱스 구하기 
            if not num[i].isdigit():
                tail = num[i:]
                num = num[:i]
                break
        
        data.append((head, num, tail))
        
    # 파일명, 번호 순으로 정렬 -> 소문자로 통일해야함 
    data.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    for i in data:
        answer.append("".join(i))
    return answer
    
input = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(input))

''' 정규 표힌식 사용 
import re 

def solution(files):
    # file의 숫자를 기준으로 split
    answer = [re.split(r"([0-9]+)", f) for f in files ]
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    
    return [ "".join(i) for i in answer]
'''
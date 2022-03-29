# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = []
    
    word = s.split(" ")
    
    for i in word:
    	# 첫글자만 대문자로 변경, 나머지는 모두 소문자 
        total = i[:1].upper() + i[1:].lower()
        answer.append(total)

    return " ".join(answer)
    
s ="for  the"
print(solution(s))
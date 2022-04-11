# https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import defaultdict

def solution(str1, str2):
    # 대문자로 통일     
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 원소별 개수 저장 
    x = defaultdict(int)
    y = defaultdict(int)
    # 교집합 개수
    inter = 0
    # 합집합 개수 
    union = 0 
    
    
    for i in range(0, len(str1)-1):
        # 두 글자씩 끊어서 공백 제거 후 
        s1 = str1[i:i+2]
        s1 = s1.replace(" ", "")
        
        # 길이가 2이고 영어로만 구성되어 있으면 
        if len(s1) == 2 and s1.isalpha() :
            # value + 1 
            x[(str1[i:i+2])] += 1 
            # 합집합 개수 + 1 
            union += 1 
            
    for i in range(0, len(str2)-1) :
        s2 = str2[i:i+2]

        if len(s2) == 2 and s2.isalpha() :
            y[str2[i:i+2]] += 1 
            union += 1 
     
     # x의 원소들에 대해        
    for i in x :
        # y에도 존재하는 원소이면, 즉 교집합이면 
        if i in y:
            # 더 작은 값 교집합의 개수에 더하기 
            inter += min(x[i],y[i])
      
    # 합집합에서 교집합 제거       
    union -= inter 
    
    # 합집합 0 이면 
    if union == 0 :
        return 65536
    
    return int(inter/union * 65536)
    
s1 = 'E=M*C^2'
s2 = 'e=m*c^2'
print(solution(s1,s2))
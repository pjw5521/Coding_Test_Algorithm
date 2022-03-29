# https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product

def solution(word):
    answer = 0
    
    words= [ 'A', 'E', 'I', 'O', 'U' ]
    dic = [] 
    for i in range(1,6):
        pro = list(product(words,repeat=i))
        
        for j in pro:
            dic.append("".join(j))
    dic.sort()
    
    return dic.index(word) +1 

word = "AAAE"
print(solution(word))
# https://programmers.co.kr/learn/courses/30/lessons/12900
# 동적 계획법 문제 
# 점화식 d[n] = d[n-1] + d[n-2]
def solution(n):
    d = [0] * n
    d[0] =1 
    d[1] =2 

    for i in range(2, n):
        # 나머지 안하면 런타임에러
        d[i] =(d[i-1] + d[i-2])%1000000007
    
    return d[n-1]
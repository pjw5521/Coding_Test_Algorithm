# https://programmers.co.kr/learn/courses/30/lessons/12945

'''
# 시간초과
def solution(n):
    answer = 0
    answer = fibo(n) % 1234567
    return answer

def fibo(n):
    if n == 0 or n == 1 :
        return n
    return fibo(n-1) + fibo(n-2)
'''

# 다이나믹 프로그래밍에서 보텀업 방식 참고 
def solution(n):
    d = [0] * n
    d[0] = 1
    d[1] = 1 
    for i in range(2, n):
    # 계산할 때마다 1234567로 나눈 나머지를 저장
        d[i] = (d[i-1] + d[i-2])%1234567
    return d[-1]
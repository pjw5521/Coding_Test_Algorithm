#https://programmers.co.kr/learn/courses/30/lessons/82612
# 간단하게 반복문으로 풀이 
def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1,count+1):
        total += i*price 
    if total > money:
        answer = abs(total-money)
        
    return answer
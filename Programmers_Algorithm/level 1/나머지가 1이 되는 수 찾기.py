#https://programmers.co.kr/learn/courses/30/lessons/87389
# for 문으로 간단하게 풀었는데 통과..
def solution(n):
    answer = 0
    for i in range(2,n):
        if n % i == 1 :
            answer = i
            break
            
    return answer
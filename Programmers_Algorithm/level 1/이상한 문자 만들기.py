#https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = []
    num = s.split(" ")
    for i in num:
        for j in range(len(i)):
            if j % 2 == 0:
                answer.append(i[j].upper())
            else:
                answer.append(i[j].lower())
        answer.append(" ")
    
    return "".join(answer[:-1])
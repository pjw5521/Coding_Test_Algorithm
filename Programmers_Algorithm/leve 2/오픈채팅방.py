# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = {}
    for i in record :
        data = i.split()
        if data[0] == 'Enter':
            answer.append(['Enter', data[1]])
            dic[data[1]] = data[2]
        elif data[0] == 'Leave':
            answer.append(['Leave', data[1]])
        else:
            dic[data[1]]= data[2]
    result = []
    for i in answer:
        if i[0] == 'Enter':
            temp = dic[i[1]] + '님이 들어왔습니다.'
            result.append(temp)
        else:
            temp = dic[i[1]] + '님이 나갔습니다.'
            result.append(temp)
    return result
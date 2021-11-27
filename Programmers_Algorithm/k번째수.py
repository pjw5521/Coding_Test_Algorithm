#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for command in commands:
        i ,j , k = command
        # array = array[i-1:j] 하면 오류
        data = array[i-1:j]
        data.sort()
        answer.append(data[k-1])
    return answer
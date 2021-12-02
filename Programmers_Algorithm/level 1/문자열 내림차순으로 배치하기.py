#https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    answer = ''
    answer = ''.join(sorted(s, reverse = True))
    return answer
#https://programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations

def solution(numbers):
    answer = []
    combine = list(combinations(numbers,2))
    for i in combine:
        answer.append(sum(i))
    answer = list(set(answer))
    answer.sort()
    return answer
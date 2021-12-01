#https://programmers.co.kr/learn/courses/30/lessons/1845
from itertools import combinations
def solution(nums):
    answer = 0
    count = len(set(nums))
    # 중복 제거 후 개수가 len(nums)//2 보다 작을 때 
    if count < len(nums)//2:
        answer = count 
    else:
        answer = len(nums)//2
    return answer
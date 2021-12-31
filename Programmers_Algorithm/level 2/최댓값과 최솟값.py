# https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    # 공백을 기준으로 나눠서 int형으로 변환하여 배열에 저장 
    data = list(map(int,s.split()))
    answer = str(min(data)) + " " + str(max(data))
    return answer
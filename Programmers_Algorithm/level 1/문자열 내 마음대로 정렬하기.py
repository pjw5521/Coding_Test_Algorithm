# https://programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    answer = []
    dic = {}
    new_dict = {}
    for i in strings:
        dic[i] = i[n]
    new_dict = dict(sorted(dic.items(), key=lambda x: (x[1],x[0])))
    return list(new_dict.keys())
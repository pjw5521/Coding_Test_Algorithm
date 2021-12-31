#https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

def solution(relation):
    col = len(relation[0])
    row = len(relation)
    index = []
    unique = []

    # 가능한 column 조합들 저장 
    for i in range(1, col+1):
        index.extend(combinations(range(col),i))

    # 각 column들 조합마다 
    for i in index:
        # 각 column들의 속성값 tuple로 저장 
        tmp = [tuple(item[index] for index in i) for item in relation]
        # 중복 제거 후 개수가 row 개수와 같다면 유일성 만족
        if len(set(tmp)) == row:
            result = True
            for k in unique:
                # 현재 후보키 column 조합들의 부분집합이면 최소성 만족 x 
                if set(k).issubset(set(i)):
                  result= False
                  break
            if result :
              unique.append(i)
    
    return len(unique)
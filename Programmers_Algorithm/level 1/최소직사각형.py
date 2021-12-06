#https://programmers.co.kr/learn/courses/30/lessons/86491
'''
각 직사각형마다 큰 길이는 row에 작은 길이는 col에 대입 
row와 col의 최댓값끼리 곱한 게 답
'''
def solution(sizes):
    answer = 0
    
    row = []
    col = []
    for i in sizes:
        row.append(max(i))
        col.append(min(i))
    
    answer = max(row) * max(col)
    
    return answer
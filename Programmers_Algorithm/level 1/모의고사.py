# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    first_ans = [1,2,3,4,5] # 5개
    second_ans = [2, 1, 2, 3, 2, 4, 2, 5] # 8개 
    third_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10 
        
        if answers[i] == first_ans[s1]:
            c1 += 1 
        if answers[i] == second_ans[s2]:
            c2 += 1
        if answers[i] == third_ans[s3]:
            c3 += 1
    
    result = max(c1,c2,c3)
    if result == c1 :
        answer.append(1)
    if result == c2:
        answer.append(2)
    if result == c3:
        answer.append(3)
            
    return answer

# 다른 사람 풀이 

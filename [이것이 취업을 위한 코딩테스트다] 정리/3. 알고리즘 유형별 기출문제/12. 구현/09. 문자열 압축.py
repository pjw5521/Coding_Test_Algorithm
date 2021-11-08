# 문제 323쪽 
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1):
        compressed = ""
        count = 1
        prev = s[0:step]
        for j in range(step,len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
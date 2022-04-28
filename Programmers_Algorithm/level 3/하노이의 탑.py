# https://programmers.co.kr/learn/courses/30/lessons/12946

# a에 있는 n-1 개의 원반을 c를 거쳐 b로 옮긴다
# a에 남은 가장 아래에 있는 원반을 c로 옮긴다

answer = []

def hanoi(n, f, to, sub):
    if n == 1 :
        answer.append((f, to))
        return
    # 1번 과정 
    hanoi(n-1, f, sub, to)
    # 2번 과정 
    answer.append((f,to))
    # 3번 과정 
    hanoi(n-1, sub, to, f)
        
def solution(n):
    hanoi(n, 1, 3, 2)
    return answer
    
n = 2
print(solution(n))
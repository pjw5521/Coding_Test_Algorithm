#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 체육복을 도난 당했을 수도 있으므로 차집합으로 만들어줘야함.
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve:
        if i-1 in set_lost:
            # 왼쪽 요소부터 제거 
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
            
    return n - len(set_lost)
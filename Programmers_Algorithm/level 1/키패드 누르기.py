#https://programmers.co.kr/learn/courses/30/lessons/67256
# 규칙 찾는 것이 중요
def solution(numbers, hand):
    answer = ''
    result = []
    # *는 10, 0은 11, #은 12로 설정
    right = 12
    left = 10 
    for i in numbers:
        if i in {1,4,7}:
            left = i
            answer += 'L'
        elif i in {3,6,9}:
            right = i
            answer += 'R'
        #상 +3 , 하 -3, 좌 +1, 우 -1 로 설정 
        #이동 거리는 3으로 나눈 몫과 나머지를 더한 값 
        elif i in {2,5,8,0}:
            if i == 0 :
                i = 11 
            left_len = abs(i-left) // 3 + abs(i-left) % 3 
            right_len = abs(i-right)// 3 + abs(i-right)% 3
            if left_len < right_len:
                left = i
                answer += 'L'
            elif left_len > right_len:
                right = i
                answer += 'R'
            else:
                if hand == 'left':
                    left = i
                    answer += 'L' 
                else :
                    right = i
                    answer += 'R'
                
    return answer
# https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    answer = 0
    
    # 최소 좌우 이동 횟수 
    min_move = len(name) - 1 
    
    for i, s in enumerate(name):
        # 알파벳 변경 최소 횟수 더하기 
        answer += min(ord(s) - ord('A') , ord('Z') - ord(s)+1)
        
        next = i + 1
        # 연속된 A 문자열 찾기 
        while next < len(name) and name[next] == 'A':
            next += 1 
            
        # 원래 횟수, 연속된 A의 왼쪽에서 시작했을 때, 연속된 A의 오른쪽에서 시작했을 때 비교하여 최솟값 갱신
        min_move = min(min_move, 2*i + len(name)-next , i + 2 *(len(name)-next))
        
    # 좌우 이동 횟수 더하기 
    answer += min_move 
    return answer
    
n = 'JAN'
print(solution(n))
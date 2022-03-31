# https://programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    n = len(land)
    
    for i in range(1, n):
        for j in range(4):
        	# i-1 행의 0열을 제외한 다른 열의 최댓값 더하기 
            if j == 0 :
                land[i][j] += max(land[i-1][1:])
            # i-1 행의 1열을 제외한 다른 열의 최댓값 더하기 
            if j == 1 :
                land[i][j] += max(max(land[i-1][2:]),land[i-1][0])
            # i-1 행의 2열을 제외한 다른 열의 최댓값 더하기 
            if j == 2 :
                land[i][j] += max(max(land[i-1][:2]),land[i-1][3])
            # i-1 행의 3열을 제외한 다른 열의 최댓값 더하기 
            if j == 3:
                land[i][j] += max(land[i-1][:-1])
                
    # 마지막 행의 최댓값 
    return max(land[-1])

land= [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	
print(solution(land))
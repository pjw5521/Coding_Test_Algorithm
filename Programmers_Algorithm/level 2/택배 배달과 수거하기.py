# https://school.programmers.co.kr/learn/courses/30/lessons/150369
def solution(cap, n, deliveries, pickups):
    answer = 0

    d = 0
    p = 0 
    
    # 먼 거리에 있는 택배부터 
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
		
        # 더이상 해당 위치까지 방문하지 않아도 될때까지 갱신 
        while d > 0 or p > 0 :
            d -= cap
            p -= cap
            answer += (i+1) * 2 

    
    return answer
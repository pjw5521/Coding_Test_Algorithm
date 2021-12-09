# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    result = 0
    while len(scoville) >= 1:
            min1 = heapq.heappop(scoville)
            if min1 >= K:
                return result 
            if not scoville :
                break
            else :
                min2 = heapq.heappop(scoville)
                heapq.heappush(scoville, min1+(min2*2))
                result +=1
    return -1
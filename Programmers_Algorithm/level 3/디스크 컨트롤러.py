#https://programmers.co.kr/learn/courses/30/lessons/42627
# 최소 힙 문제 
import heapq 
def solution(jobs):
    answer =0 
    now = 0 
    i = 0 
    start = -1 
    heap = [] 
    while i < len(jobs):
        for arr_time, job in jobs:
            # 도착시간이 이전 job의 실행 시간과 실행 완료 시간의 사이라면 힙에 push 
            if start < arr_time <= now :
                # 일하는 시간 기준으로 최소힙 구현 
                heapq.heappush(heap, (job,arr_time))
                
        if heap:
            job, arr_time = heapq.heappop(heap)
            start = now 
            now += job
            # 작업 요청시간부터 작업 종료 시간 계산 
            answer += (now - arr_time)
            i += 1
        # heap이 비었다면 현재 시간 +1 
        else:
            now += 1 
        # 평균 구하기
    return answer// len(jobs)
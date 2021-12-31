#https://programmers.co.kr/learn/courses/30/lessons/43164
from collections import deque

def solution(tickets):
    
    routes = dict()
	
    # 출발지를 Key, 도착지를 value 로 저장 
    for t1, t2 in tickets:

        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]

	# value 내림차순 정렬 
    for k in routes.keys():
      routes[k].sort(reverse = True)

    stack = deque()
    # stack에 출발지 추가 
    stack.append('ICN')
    answer = []

    while stack:
      start = stack[-1]
      # 딕셔너리에 key가 없거나 key의 value가 없다면 
      if start not in routes or  len(routes[start]) == 0:
      # answer에 추가 
        answer.append(stack.pop())
      else :
      # key의 value 하나 빼고 stack에 추가 
        stack.append(routes[start][-1])
        routes[start].pop()

    answer.reverse()

    return answer
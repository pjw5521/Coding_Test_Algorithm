#https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque

def solution(n, computers):
    answer = 0 
    visited = [False] * (n)
    
    for i in range(n):
      if visited[i] == False :
        bfs(computers, i, visited, n)
        answer += 1 

    return answer

def bfs(computers, start, visited, n):
  q = deque()
  q.append(start)

  while q:
    x = q.popleft()
    visited[x] = True
    for i in range(n):
      if computers[x][i] == 1 and visited[i] == False:
        visited[i] = True
        q.append(i)
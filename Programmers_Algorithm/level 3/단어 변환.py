#https://programmers.co.kr/learn/courses/30/lessons/43163
# bfs/ dfs 문제 

from collections import deque
def solution(begin, target, words):
    
    # target이 words에 없어 변환할 수 없을때 
    if target not in words : 
      return 0
    
    visited = [False] * len(words)

    answer = bfs(begin, target, visited, words)
    
    return answer

def bfs(begin, target, visited, words):
  q = deque()
  q.append((begin,0))

  while q :
    word, depth = q.popleft()
    
    # word가 target일 때 
    if word == target:
      return depth

    for i in range(len(words)):
      if visited[i] :
        continue

      count = 0 
    # 단어 비교
      for a, b in zip(word, words[i]):
        if a!=b :
          count += 1 
      # 다른 알파벳이 1개 뿐일 때 큐에 대입, 방문 기록 
      if count == 1 :
        q.append((words[i], depth+1))
        visited[i]= True 
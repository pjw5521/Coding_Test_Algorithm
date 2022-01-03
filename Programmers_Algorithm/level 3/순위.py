#https://programmers.co.kr/learn/courses/30/lessons/49191
from collections import defaultdict
def solution(n, results):
  answer = 0
  # value가 set -> 중복 제거 
  winner_graph= defaultdict(set)
  loser_graph=defaultdict(set)

  for winner, loser in results:
    # 이긴 애들 
    winner_graph[winner].add(loser)
    # 진 애들 
    loser_graph[loser].add(winner)
  
  for i in range(1,n+1):
    # i한테 진 애들 
    for loser in winner_graph[i]: # i한테 진애들은 i를 이긴 애들한테도 진것 
        loser_graph[loser].update(loser_graph[i])

    # i한테 이긴 애들 
    for winner in loser_graph[i]:
      # i한테 이긴 애들은 i한테 진 애들도 이긴 것 
        winner_graph[winner].update(winner_graph[i])

 # i가 이긴 애들과 진 애들의 수의 합이 n-1이라면 순위 매기기 가능 
  for i in range(1, n+1):
    if len(loser_graph[i]) + len(winner_graph[i]) == n-1:
      answer += 1

  
  return answer
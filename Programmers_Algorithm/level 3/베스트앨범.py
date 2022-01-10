# https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict

def solution(genres, plays):
  answer = []
  play_dic = defaultdict(list)
  genre_dic = defaultdict(int)

  for i in range(len(genres)):
    genre_dic[genres[i]] += plays[i]
    play_dic[genres[i]].append((i, plays[i]))
 
  items = sorted(genre_dic, key = lambda x : genre_dic[x],reverse=True)
  
  
  for item in items:
    tmp = sorted(play_dic[item], key = lambda x : x[1],reverse=True)
    for idx, play in tmp[:2]:
      answer.append(idx)

  return answer
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

'''
from collections import defaultdict

def solution(genres, plays):
  answer = []
  # 장르별 총 재생수 
  genre_dic = defaultdict(int)
  # 장르 별 노래
  play_dic = defaultdict(list)

  for i in range(len(genres)):
    genre_dic[genres[i]] += int(plays[i])
    play_dic[genres[i]].append((i, plays[i]))

  genre_dic = sorted(genre_dic, key = lambda x: genre_dic[x], reverse = True)
  
  for genre in genre_dic:
    tmp = sorted(play_dic[genre], key = lambda x : x[1], reverse = True)
    if len(tmp) > 1 :
      for i in range(2):
        answer.append(tmp[i][0])
    else:
      answer.append(tmp[0][0])

  return answer
  '''
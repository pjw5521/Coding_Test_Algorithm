#https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations 

def solution(user_id, banned_id):
  # 가능한 banned_id 조합 모두. 어떤 banned_id에 해당되는지에 따라 결과 달라지므로 순열 사용 
  permute = list(permutations(user_id,len(banned_id)))
  answer = []
  for users in permute:
      # banned_id 에 해당하는지 체크 
    if not check(users,banned_id):
      continue
      # banned_id의 조합에 해당될 수 있으면 
    else :
        # set으로 변환하여 중복 제거 
      users = set(users)
      # answer에 없으면 추가 
      if users not in answer:
        answer.append(users)
    # 개수 반환 
  return len(answer)

def check(users, banned_id):
  
  for i in range(len(users)):
    # 길이 다르면 같지 않음 
    if len(users[i]) != len(banned_id[i]):
      return False

    for j in range(len(users[i])):
        # *이면 continue 
      if banned_id[i][j] == '*':
        continue
        # 한 글자라도 다르면 같지 않음 
      if users[i][j] != banned_id[i][j]:
        return False
  
  return True
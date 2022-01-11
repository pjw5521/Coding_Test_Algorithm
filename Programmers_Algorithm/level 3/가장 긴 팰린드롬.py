#https://programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
  answer = 0
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      # 팰린드롬이라면
      if check(s[i:j]):
        # 길이 긴 걸로 갱신 
        answer = max(answer,len(s[i:j]))
  return answer

def check(x):
  # 좌우 대칭인지 확인 
  if x == x[::-1]:
    return True

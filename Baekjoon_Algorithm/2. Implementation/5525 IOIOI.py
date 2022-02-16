# https://www.acmicpc.net/problem/5525﻿
n = int(input())

m = int(input())

s = input()

# 인덱스 
i = 0 
# IOI가 반복되는 횟수 저장 
cnt = 0 
# IOI가 n만큼 반복되는 구간 개수 
answer = 0 

while i < m-1:
  if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == "I":
    # IOI가 반복되는 횟수 증가
    cnt += 1 
    # IOI가 n만큼 반복되면
    if cnt == n:
      answer += 1 
      cnt -= 1
    # 인덱스 2 증가시키기 
    i += 1 
  else:
    # IOI가 반복되는 횟수 초기화 
    cnt = 0 
  i += 1 

print(answer)
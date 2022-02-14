# https://www.acmicpc.net/problem/9375
from collections import defaultdict

test = int(input())

for _ in range(test):
  
  n = int(input())

  dic = defaultdict(int)

  # 의상 종류별 의상 개수 저장 
  for _ in range(n):
    data = input().split()
    
    dic[data[1]] += 1 

  cnt = 1
  # 경우의 수 계산 
  for i in dic:
    cnt *= dic[i] + 1 
  
  print(cnt - 1)
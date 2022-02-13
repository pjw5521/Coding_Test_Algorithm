# https://www.acmicpc.net/problem/1764
from collections import defaultdict
n, m = map(int,input().split())

dic = defaultdict(int)
for _ in range(n):
  s = input()
  dic[s] += 1 

for _ in range(m):
  s = input()
  dic[s] += 1 

# 사람 이름 저장 
answer = []
# 총 사람 수 저장 
cnt = 0 
for i in dic:
  if dic[i]== 2 :
    answer.append(i)
    cnt += 1 

print(cnt)
# 사전 순으로 정렬 
answer.sort()
for i in answer:
  print(i)
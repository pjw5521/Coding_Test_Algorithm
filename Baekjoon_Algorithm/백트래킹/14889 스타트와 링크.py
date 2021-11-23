#https://www.acmicpc.net/problem/14889
from itertools import combinations
n = int(input())

data = []
num = [ i for i in range(n) ]

for _ in range(n):
  data.append(list(map(int,input().split())))

combine = list(combinations(num, n//2))

min_value = 100 * n * n 
for case_a in combine:
  result_a = 0 
  result_b = 0
  for i in case_a:
    for j in case_a:
      result_a += data[i][j]
  # 상대팀은 case_a 여집합 
  case_b= [ x for x in range(n) if x not in case_a]

  for i in case_b:
    for j in case_b:
      result_b += data[i][j]
  min_value= min(min_value, abs(result_a - result_b))

print(min_value)
  
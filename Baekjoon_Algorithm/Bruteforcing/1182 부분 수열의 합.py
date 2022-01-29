# https://www.acmicpc.net/problem/1182
from itertools import combinations

n, s = map(int,input().split())

data = list(map(int,input().split()))

count = 0 

# 모든 부분 수열의 합을 구해서 s와 같을 때 count + 1 
for i in range(1, n+1):
  combine = list(combinations(data,i))
  for num in combine:
    if sum(num) == s :
      count += 1 

print(count)
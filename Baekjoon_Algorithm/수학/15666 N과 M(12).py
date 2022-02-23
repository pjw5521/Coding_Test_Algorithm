# https://www.acmicpc.net/problem/15666
from itertools import combinations_with_replacement

n, m = map(int,input().split())

data = list(map(int,input().split()))
data.sort()

combine = list(combinations_with_replacement(data,m))

combine = list(set(combine))
combine.sort()

for i in combine:
  print(*i)
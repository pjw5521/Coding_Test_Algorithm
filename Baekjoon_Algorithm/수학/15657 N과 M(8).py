# https://www.acmicpc.net/problem/15657
from itertools import combinations_with_replacement

n, m = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
combine = list(combinations_with_replacement(data,m))

for i in combine:
  print(*i)
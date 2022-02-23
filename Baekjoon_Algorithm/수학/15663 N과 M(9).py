# https://www.acmicpc.net/problem/15663
from itertools import permutations

n, m = map(int,input().split())

data = list(map(int,input().split()))

combine = list(permutations(data,m))

combine = list(set(combine))
combine.sort()

for i in combine:
  print(*i)
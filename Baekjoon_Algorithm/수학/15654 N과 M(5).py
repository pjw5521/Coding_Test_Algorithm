# https://www.acmicpc.net/problem/15654
from itertools import permutations

n, m = map(int,input().split())

data = list(map(int,input().split()))

combine = list(permutations(data,m))

combine.sort()
for i in combine:
  print(*i)
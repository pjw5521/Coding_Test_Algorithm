# https://www.acmicpc.net/problem/15651
# 중복순열
import sys
from itertools import product
input = sys.stdin.readline

n ,m = map(int,input().split())

data = [ i+1 for i in range(n)]

combine = list(product(data, repeat = m))

combine .sort()

for i in combine:
  print(*i)
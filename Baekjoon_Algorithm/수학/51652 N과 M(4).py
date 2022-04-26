# https://www.acmicpc.net/problem/15652
# 중복 조합 
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n ,m = map(int,input().split())

data = [ i+1 for i in range(n)]

combine = list(combinations_with_replacement(data, m))

combine .sort()

for i in combine:
  print(*i)
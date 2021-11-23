# https://www.acmicpc.net/problem/15650
# 조합 
import sys
from itertools import combinations
input = sys.stdin.readline

n ,m = map(int,input().split())

data = [ i+1 for i in range(n)]

combine = list(combinations(data,m))

combine .sort()

for i in combine:
  print(*i)
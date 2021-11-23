# https://www.acmicpc.net/problem/15649
# 순열 
import sys
from itertools import permutations
input = sys.stdin.readline

n ,m = map(int,input().split())

data = [ i+1 for i in range(n)]

permute = list(permutations(data,m))

permute .sort()

for i in permute:
  print(*i)
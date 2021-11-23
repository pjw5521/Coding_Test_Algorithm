#https://www.acmicpc.net/problem/2798
import sys
input = sys.stdin.readline

from itertools import combinations 

n, m = map(int,input().split())

data= list(map(int,input().split()))

combine = list(combinations(data,3))

result = 0 
for i in combine:
  if sum(i) <= m:
    result = max(result, sum(i))

print(result)
# https://www.acmicpc.net/problem/5568
from itertools import permutations
import sys

input = sys.stdin.readline 
n = int(input())

k = int(input())

data = [] 
for _ in range(n):
  data.append(int(input()))

# 순열 구하기 
permute = list(permutations(data,k))

result = set()
for i in permute:
  # 숫자들을 연결해야 하므로 문자로 바꿔서 
  s = "".join(map(str,i))
  result.add(s)

print(len(result))

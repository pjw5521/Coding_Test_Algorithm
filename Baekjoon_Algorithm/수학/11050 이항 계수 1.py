# https://www.acmicpc.net/problem/11050
# 조합 개수 구하기 
n, k = map(int,input().split())

answer = 1 

for _ in range(k):
  answer *= n 
  n -= 1

for _ in range(k):
  answer /= k
  k -= 1 

print(int(answer))
#https://www.acmicpc.net/problem/2231
import sys
input = sys.stdin.readline

n = int(input())

i = 1
while True:
  result = i
  for j in str(i):
    result += int(j)
  if result == n:
    break
  if i > n:
    i = 0
    break
  i +=1

print(i)


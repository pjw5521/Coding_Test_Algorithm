# https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
  a, b = map(int,input().split())
  data.append((a,b))

data.sort(key = lambda x : (x[0], x[1]))

for a,b in data:
  print(a, end=" ")
  print(b)

'''
다른 코드
n = int(input())

data =[]
for _ in range(n):
  x, y = map(int,input().split())
  data.append((x,y))

data.sort(key = lambda x : (x[0], x[1]))

for a, b in data:
  print(a, b)
'''
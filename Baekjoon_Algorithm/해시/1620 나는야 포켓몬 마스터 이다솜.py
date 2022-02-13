# https://www.acmicpc.net/problem/1620
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dic = {}

for i in range(1,n+1):
  x = input().strip()
  dic[i] = x
  dic[x] = i
  
for _ in range(m):
  s = input().strip()

  if s.isdigit() :
    print(dic[int(s)])
  else:
    print(dic[s])
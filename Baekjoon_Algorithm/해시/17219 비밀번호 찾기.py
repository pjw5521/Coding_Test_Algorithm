# https://www.acmicpc.net/problem/17219
n, m = map(int,input().split())

dic = dict()

for _ in range(n):
  s, p = input().split()
  dic[s] = p

for _ in range(m):
  s = input()
  print(dic[s])


# 문제 https://www.acmicpc.net/problem/1920
n = int(input())
A = set(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))

for i in B:
  if i in A:
    print("1")
  else:
    print("0")
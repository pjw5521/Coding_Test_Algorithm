#https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input())
word = []

for _ in range(n):
  word.append(input())

# set으로 중복 제거 후 다시 list
word = list(set(word))

word.sort(key=lambda x : (len(x), x))

for i in word:
  print(i, end ="")
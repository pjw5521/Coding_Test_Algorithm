# https://www.acmicpc.net/problem/1436
n = int(input())

name = 666

count = 0

while True:

  if count == n:
    break
  
  if '666' in str(name):
    count += 1

  name += 1

print(name-1)
# https://www.acmicpc.net/problem/1431
import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
  data.append(input())

def sum_num(n):
  result = 0 
  for i in n:
    if i.isdigit():
      result += int(i)
  return result 

data.sort(key= lambda x : (len(x), sum_num(x), x))

for i in data:
  print(i,end ="")
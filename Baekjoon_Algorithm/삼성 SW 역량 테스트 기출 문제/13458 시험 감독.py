# https://www.acmicpc.net/problem/13458
# 구현 문제 

n = int(input())

people = list(map(int,input().split()))

a, b = map(int,input().split())
count = 0 
for i in people:
  count +=1 
  i -= a
  
  if i > 0 :
    count += i // b 
    if i % b != 0:
      count += 1 

print(count)
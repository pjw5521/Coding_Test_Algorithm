# https://www.acmicpc.net/problem/1676
num = int(input())

d = 2

two = 0
five = 0 

# 소인수분해 
for n in range(1, num+1):
  d = 2
  while d <= n:
    if n % d == 0:
      n = n // d 
      # 2의 개수
      if d == 2 :
        two += 1 
      # 5의 개수 
      if d == 5:
        five += 1 
    else:
      d = d + 1 
    
print(min(two,five))
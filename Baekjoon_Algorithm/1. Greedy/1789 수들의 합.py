# https://www.acmicpc.net/problem/1789
n = int(input())

count = 0
start = 1
result = 0
while True:
  result += start 
  count += 1 
  if result <= n:
    start += 1 
  else:
    count -= 1
    print(count)
    break
  

#https://www.acmicpc.net/problem/1065
n = int(input())

start = 1
count = 0

while True:
  
  if start > n :
    break
  
  tmp = str(start)

  if len(tmp) < 3:
      count += 1
  else :
    if int(tmp[2])-int(tmp[1]) == int(tmp[1]) - int(tmp[0]):
      count += 1 

  start += 1 

print(count)
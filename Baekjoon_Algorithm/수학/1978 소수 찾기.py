# https://www.acmicpc.net/problem/1978
n = int(input())

data = list(map(int,input().split()))

cnt = 0 

for i in data:
  result = True 
  if i == 1 :
    continue
  else :
    for j in range(2, int(i** 0.5)+1):
      if i % j == 0:
        result = False 
        break
    if result :
      cnt += 1 

print(cnt)
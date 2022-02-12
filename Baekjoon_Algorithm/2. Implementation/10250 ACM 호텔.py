# https://www.acmicpc.net/problem/10250
test = int(input())

for _ in range(test):
  h, w, n = map(int,input().split())
  
  # 마지막 층일 때 
  if n % h == 0:
    answer = str(h) + str(n//h).zfill(2)
  else :
    answer = str(n%h) + str(n//h + 1).zfill(2)

  print(answer)
#문제 315쪽 
n, m = map(int,input().split())

data = list(map(int,input().split()))

count = 0 
for a in range(n):
  for b in range(a+1,n):
    if data[a] != data[b]:
      count += 1 

print(count)
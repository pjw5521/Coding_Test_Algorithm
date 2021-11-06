# 문제 314쪽

n = int(input())

data = list(map(int,input().split()))
data.sort()
result = 1

for i in data:
  if result < i :
    break
  else:
    result += i

print(result)
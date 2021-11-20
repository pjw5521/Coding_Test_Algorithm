n = int(input())

d = []

for i in range(n):
  num = int(input())
  if (num != 0):
    d.append(num)
  else:
    del d[-1]
  
result = 0
for i in d:
  result += i

print(result)
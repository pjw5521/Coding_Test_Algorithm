#https://www.acmicpc.net/problem/1541
n = input().split('-')
result = 0
print(n)

for i in n[0].split('+'):
  result += int(i)

for i in n[1:]:
  for j in i.split('+'):
    result -= int(j) 

print(result)
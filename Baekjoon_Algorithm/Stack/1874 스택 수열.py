# https://www.acmicpc.net/problem/1874
n = int(input())

i = 1
stack =[]
answer = []
result = True

for _ in range(n):
  num = int(input())

  while i <= num:
    stack.append(i)
    answer.append('+')
    i += 1
  
  if stack[-1] == num:
    stack.pop()
    answer.append('-')
  else:
    result = False

if result :
  for k in answer:
    print(k)
else:
  print('NO')
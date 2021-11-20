#https://www.acmicpc.net/problem/4796
count = 1
while True:
  a, b, c = map(int,input().split())
  if a == 0 and b == 0 and c == 0:
    break
  result = (c//b) * a + min(c % b, a)
  print("Case ",end ="")
  print(count,end ="")
  print(":",end= " ")
  print(result) 
  count += 1 
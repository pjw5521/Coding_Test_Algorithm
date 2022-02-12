# https://www.acmicpc.net/problem/4153
while True :
  data = list(map(int,input().split()))
  
  data = sorted(data)
  a,b,c = map(int,data)

  if a== 0 and b == 0 and c==0:
    break

  if a== 0 or b == 0 or c==0:
    print('wrong')
    continue

  if c*c == a*a + b*b:
    print('right')
  else:
    print('wrong')
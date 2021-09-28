# 풀이 다양
n = int(input())
x, y = 1,1 
plans = input().split()

for i in plans:
  if( i == "R"):
    if( y == n ):
      continue
    y += 1
  elif( i == "U"):
    if( x == 1 ):
      continue
    x -= 1
  elif( i == "L"):
    if( y == 1 ):
      continue
    y -= 1
  elif( i == "D"):
    if( x == n  ):
      continue
    x += 1

print(x,y)
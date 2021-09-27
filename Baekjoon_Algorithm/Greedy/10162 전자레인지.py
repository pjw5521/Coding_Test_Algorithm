n = int(input())
d = [ 300, 60 , 10 ]
a = []

for i in d:
   a.append(n // i)
   n = n % i

if( n != 0 ):
  print(-1)
else:
  for i in a:
    print(i ,end = " ")
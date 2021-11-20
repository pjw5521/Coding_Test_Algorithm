a, b = map(int, input().split())

d = []
for i in range(a):
  n = int(input())
  d.append(n)

d.sort()
d.reverse()
count = 0
for i in d:
  if( b == 0):
    break
  count += b // i
  b = b % i
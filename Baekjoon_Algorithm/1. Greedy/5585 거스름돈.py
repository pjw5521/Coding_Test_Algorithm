#https://www.acmicpc.net/problem/5585
n = 1000 - int(input())

a = [500, 100, 50, 10, 5, 1]
count = 0 
for i in a:
  count += n // i
  n = n % i

print(count)
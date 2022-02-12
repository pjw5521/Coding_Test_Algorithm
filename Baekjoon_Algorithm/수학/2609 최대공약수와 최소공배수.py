# https://www.acmicpc.net/problem/2609
'''
#시간 초과 
n, m = map(int,input().split())

for i in range(min(n,m), 0, -1):
  if n % i == 0 and m % i == 0 :
    print(i)
    break

for j in range(max(n,m), n*m+1):
  if j % n == 0 and j % m == 0 :
    print(j)
    break
'''
n, m = map(int,input().split())

#최대 공약수 
def gcd(x,y):
  while(y):
    x, y = y, x%y 
  return x

print(gcd(n,m))

# 최소 공배수
def lcm(x,y):
  return (x*y) // gcd(x,y)

print(lcm(n,m))

'''
내장 함수 사용 
import math 

n, m = map(int,input().split())

print(math.gcd(n,m))

print(math.lcm(n,m))

'''
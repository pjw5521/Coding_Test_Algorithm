# https://www.acmicpc.net/problem/2522
n = int(input())

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)
    
for i in range(1, n):
    print(" "* i + "*" * (n-i))
#https://www.acmicpc.net/problem/2441
n = int(input())

for i in range(n,0,-1):
    print(" " *(n-i)+ '*' * i )
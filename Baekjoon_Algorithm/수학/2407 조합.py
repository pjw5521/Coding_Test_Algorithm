# https://www.acmicpc.net/problem/2407
import math 

n, m = map(int,input().split())

answer = math.factorial(n) // (math.factorial(n-m) * math.factorial(m))

print(int(answer))
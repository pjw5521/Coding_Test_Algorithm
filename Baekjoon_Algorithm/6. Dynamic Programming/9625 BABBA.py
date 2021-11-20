# 문제 https://www.acmicpc.net/problem/9625
# 점화식 : a와 b 모두 피보나치 수열을 따름 

n = int(input())

fib = [0] * (n+1)
fib[1] = 1

for i in range(2, n+1):
  fib[i] = fib[i-1] + fib[i-2]

print(fib[n-1], fib[n])

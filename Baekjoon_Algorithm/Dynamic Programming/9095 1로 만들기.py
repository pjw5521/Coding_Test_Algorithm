# 문제 https://www.acmicpc.net/problem/9095
# 점화식 f(n) = f(n-1) + f(n-2) + f(n-3)
test_num = int(input())

def sol(n):
  if n == 1 : 
    return 1
  if n == 2 :
    return 2
  if n == 3:
    return 4
  
  return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(test_num):
  n = int(input())
  result = sol(n)
  print(result)


# 재귀함수로 피보나치 수열 구현 
# 페이지 212쪽 
d = [0] * 100

def fibo(x):
  if x == 1 or x == 2 :
    return 1 

  if d[x] != 0 :
    return d[x]
  
  d[x] = fibo(x-1) + fibo(x-2)

  return d[x]

print(fibo(99))
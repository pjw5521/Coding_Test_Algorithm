# 피보나치 수열 반복문으로 구현 
# 페이지 215 쪽 
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d(n))
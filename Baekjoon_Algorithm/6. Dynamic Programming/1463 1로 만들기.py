#https://www.acmicpc.net/problem/1463
# 처음에 일부만 맞았던 이유는 6의 배수를 고려해주지 않았기 때문 
n = int(input())

ans = [0] * (n+1)

if n == 1 :
  print(0)
elif n == 2 or n == 3:
  print(1)
else: 
  ans[1] = 0
  ans[2] = 1
  ans[3] = 1

  for i in range(4,n+1):
    
    if i % 3 == 0 and i % 2 == 0 :
      ans[i] = 1 + min(ans[i-1],ans[i//3], ans[i//2])
    elif i % 3 == 0 :
      ans[i] = 1 + min(ans[i-1],ans[i//3])
    elif i % 2 == 0 :
      ans[i] = 1 + min(ans[i-1],ans[i//2])
    else:
      ans[i] = 1 + ans[i-1]

  print(ans[n])
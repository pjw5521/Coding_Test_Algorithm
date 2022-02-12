n = int(input())

count = 0
while(n >= 0):
  if(n % 5 == 0 ):
    count += n //5 
    print(count)
    break
  n -= 3 
  count += 1
else :
  print(-1)

''' 다른 풀이 
n = int(input())

answer = 0 

# 5개의 봉투 수를 계속 늘려가면서 가능한 값 구하기 
for i in range(n // 5+1):
  tmp = n - i * 5 
  if tmp % 3 == 0 :
    answer = i + tmp // 3 

if not answer :
  print(-1)
else:
  print(answer)
'''
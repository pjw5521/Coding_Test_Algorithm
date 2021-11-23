# https://www.acmicpc.net/problem/1003

'''
문제에서 제시한 피보나치 수열을 실제로 수행해서 계산하면 시간 초과
규칙찾아서 풀어야함 
'''

# 아래 코드 시간 초과
# 매우 직관적으로 푼 문제 
'''
import sys
input = sys.stdin.readline
test_num = int(input())
count_zero = 0
count_first = 0

def fibo(x):
  global count_zero
  global count_first 
  if x == 0:
    count_zero += 1 
    return 1 

  if x== 1:
    count_first += 1 
    return 1

  return fibo(x-1) + fibo(x-2)

for _ in range(test_num):
  n = int(input())
  fibo(n)

  print(count_zero, end= " ")
  print(count_first)

  count_zero = 0
  count_first = 0 

'''

'''
0의 횟수 = 0의 횟수[j-1] + 0의 횟수[j-2]
1의 횟수 = 1의 횟수[j-1] + 1의 횟수[j-2]
'''
import sys
input = sys.stdin.readline
test_num = int(input())

count_zero = [ 1 , 0 ] # 0과 1의 0의 횟수 피보나치 수열 미리 저장
count_one= [ 0, 1 ] # 0과 1의 1의 횟수 피보나치 수열 미리 저장

for _ in range(test_num):
  n = int(input())
  
  if n == 0 :
    print("1 0")
  elif n == 1:
    print("0 1")
  else:
    for j in range(2, n+1):
      count_zero.append(count_zero[j-1] + count_zero[j-2])
      count_one.append(count_one[j-1] + count_one[j-2])
    print(f'{count_zero.pop()} {count_one.pop()}')
    count_zero = [ 1 , 0 ]
    count_one= [ 0, 1 ]

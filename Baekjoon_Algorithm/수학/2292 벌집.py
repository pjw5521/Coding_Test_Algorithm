# https://www.acmicpc.net/problem/2292
n = int(input())

# 벌집의 개수 1개부터 시작 
num = 1
# 방의 개수 1개부터 시작 
answer = 1 

while n > num:
  # 벌집의 개수가 6의 배수씩 증가 
  num += 6 * answer
  answer += 1

print(answer)
# 문제 https://www.acmicpc.net/problem/10610
# 30의 배수 조건 : 마지막 0, 나머지 자리수 모두 더해서 3의 배수

#list로 안 받으면 sort 안됨
n = list(input())
n.sort(reverse= True)

total = 0
# 0이 없으면 -1 출력 
if '0' not in n:
  print("-1")
else:
  for i in n:
    total += int(i)
  # 자릿수의 합이 3의 배수가 아니면 -1 출력 
  if total % 3 != 0:
    print("-1")
  else:
    print("".join(n))
# 문제 https://www.acmicpc.net/problem/9655
# 상근이가 처음 게임을 시작하므로, 상근이는 처음에 1개 또는 3개 가져갈 수 있음 -> n-1 or n-3
# 두번째 차례에서 상근이는 1개 또는 3개 가져갈 수 있음 -> n-2, n-4, n-4, n-6  
# 홀수 개 일 경우 상근이 승, 짝수 개 일 경우 창영이 승 

n = int(input())

if n % 2 == 0:
  print("CY")
else :
  print("SK")
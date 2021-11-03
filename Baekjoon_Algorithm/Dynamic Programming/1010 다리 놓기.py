# 문제 https://www.acmicpc.net/problem/1010
# 조합 이용해서 풀 수 있음 
import math 
test_num = int(input())

for i in range(test_num):
 # 서쪽 사이트의 개수는 n, 동쪽 사이트의 개수 m ( n <= m )
 # mCn : 서로 다른 m개 중에 순서 고려하지 않고 n개 선택 
 # mCn = m! / n!(m-n)!
  n, m = map(int,input().split())
  result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
  print(result)
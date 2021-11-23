# https://www.acmicpc.net/problem/18870
# 반복문 사용 시 시간 초과
# dict, sort, set 사용 
# 정렬 문제 시간초과시 dic 사용 생각해볼 것 ! 

# 아래 코드 시간 초과 
'''
import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

list_data = list(set(data))
list_data.sort()

for i in data:
  count = 0 
  for j in list_data:
    if i > j:
      count += 1
    else:
      break
  print(count, end = " ")
'''

import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

list_data = list(set(data))
list_data.sort()
dic = {}

for i in range(len(list_data)):
  dic[list_data[i]] = i

for i in range(n):
  data[i] = dic[data[i]]

print(*data)
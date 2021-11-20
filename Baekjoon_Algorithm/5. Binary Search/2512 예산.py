# https://www.acmicpc.net/problem/2512

import sys
input =  sys.stdin.readline
n = int(input())

data = list(map(int,input().split()))

total = int(input())

result = 0 

if sum(data) <= total:
  print(max(data))
else:
  start = 0
  end = max(data)
  while start <= end:
    mid = (start + end)//2
    sum_data = 0 
    for i in data:
      if i <= mid :
        sum_data += i
      else:
        sum_data += mid 
    if sum_data <= total :
      start = mid + 1 
      result = mid 
    else:
      end = mid - 1 

  print(result)

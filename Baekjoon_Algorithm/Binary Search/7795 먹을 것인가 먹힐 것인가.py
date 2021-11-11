# https://www.acmicpc.net/problem/7795
import sys
input = sys.stdin.readline

def binary_search(data, target):
  start = 0
  end = len(data) -1
  
  result = -1
  while start <= end :
    mid = ( start + end ) //2
    if data[mid] < target:
      start = mid + 1 
      result = mid 
    else:
      end = mid - 1
  return result 

test_num = int(input())

# B에서 A보다 작은 위치 result에 저장, result + 1 은 A보다 작은 B의 개수
for _ in range(test_num):
  n, m = map(int, input().split())
  data_A = list(map(int,input().split()))
  data_B = list(map(int,input().split()))
  data_A.sort()
  data_B.sort()
  count = 0 

  for i in data_A:
    count +=  binary_search(data_B, i) + 1 
  
  print(count)
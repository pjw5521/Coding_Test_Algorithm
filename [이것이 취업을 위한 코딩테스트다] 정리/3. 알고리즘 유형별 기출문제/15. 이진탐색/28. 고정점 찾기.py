# 문제 368쪽

n = int(input())

data = list(map(int,input().split()))

def binary_search(array, start ,end):
  while start <= end:
    mid = (start + end) // 2
    if data[mid] == mid:
      return mid
    elif data[mid] < mid:
      start = mid + 1 
    else: 
      end = mid - 1 
  return None

index = binary_search(data, 0, n-1)

if index == None:
  print(-1)
else:
  print(index)
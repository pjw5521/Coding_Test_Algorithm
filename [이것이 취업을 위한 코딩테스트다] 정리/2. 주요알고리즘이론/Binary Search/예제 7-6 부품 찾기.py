#  페이지 197쪽
# 이진 탐색 외에도 집합이나 계수정렬로도 해결할 수 있음 

def binary_search(array,target, start, end):
  while start <= end:
    mid = ( start + end ) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return None

n = int(input())

data= list(map(int,input().split()))

data.sort()

m = int(input())
search= list(map(int,input().split()))

for i in search:
  result = binary_search(data,i,0,n-1)
  if result == None:
    print("no",end=" ")
  else: 
    print("yes",end = " ")
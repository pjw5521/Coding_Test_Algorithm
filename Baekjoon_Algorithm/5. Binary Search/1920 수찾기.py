# 문제 https://www.acmicpc.net/problem/1920
# 두번 품 
n = int(input())
A = set(map(int,input().split()))

m = int(input())
B = list(map(int,input().split()))

for i in B:
  if i in A:
    print("1")
  else:
    print("0")


# 이진 탐색 사용한 다른 풀이 
n = int(input())

dataA = list(map(int,input().split()))

dataA.sort()

m = int(input())

dataB = list(map(int, input().split()))

def binary_search(array, target, start ,end):
  while start <= end:
    mid = (start + end) // 2
    if dataA[mid] == target:
      return mid
    elif dataA[mid] <  target:
      start = mid + 1 
    else: 
      end = mid - 1 
  return None

for i in dataB:
  result = binary_search(dataA, i, 0, n-1)
  if result == None:
    print(0)
  else:
    print(1)



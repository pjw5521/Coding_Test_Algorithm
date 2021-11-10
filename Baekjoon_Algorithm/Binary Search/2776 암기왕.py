#https://www.acmicpc.net/problem/2776
test_num = int(input())


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

for _ in range(test_num):
  n = int(input())

  dataA = list(map(int,input().split()))

  dataA.sort()

  m = int(input())

  dataB = list(map(int, input().split()))

  for i in dataB:
    result = binary_search(dataA, i, 0, n-1)
    if result == None:
      print(0)
    else:
      print(1)

# 문제 https://www.acmicpc.net/submit/2805
# 수의 범위가 매우 크기 때문에 이진탐색 의심할 것 
n, m = map(int, input().split())

data = list(map(int,input().split()))

start = 0 
end = max(data)
result = 0 

while start <= end:
  total = 0 
  mid = ( start + end ) //2
  for i in data:
    a = i - mid
    if a > 0 :
      total += a
  if total >= m :
    result = mid 
    start = mid + 1
  else:
    end = mid - 1

print(result)
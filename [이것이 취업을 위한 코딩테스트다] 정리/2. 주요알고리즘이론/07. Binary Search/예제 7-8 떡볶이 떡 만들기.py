# 페이지 201쪽
n, m = map(int,input().split())

data = list(map(int,input().split()))

start = 0 
# 떡 길이 최댓값
end = max(data)

result = 0
while (start <= end) :
  total = 0
  mid = ( start + end ) //2
  for i in data:
    if i > mid:
      total += i - mid 
  # 왼쪽 부분 탐색
  if total < m:
    end = mid -1 
  # 오른쪽 부분 탐색, 최댓값구하기 
  else :
    result = mid
    start = mid +1 

print(result)
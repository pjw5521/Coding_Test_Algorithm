# 문제 311쪽 
n = int(input())

data = list(map(int, input().split()))
# 오름차순으로 정렬
data.sort()

result = 0
count = 0

for i in data:
  count += 1
  # 포함된 명수가 공포도보다 크거나 같으면 result + 1 
  if count >= i:
    result += 1 
    count = 0 

print(result)

  
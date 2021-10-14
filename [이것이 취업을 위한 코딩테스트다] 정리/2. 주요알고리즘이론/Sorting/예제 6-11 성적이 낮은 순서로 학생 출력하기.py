# 페이지 180쪽
# 기본 정렬 라이브러리 사용
n = int(input())

data = []
for _ in range(n):
  name, score = input().split()
  data.append((name, int(score)))

# score 기준으로 오름차순 정렬
data = sorted(data, key= lambda data: data[1])

for i in data:
  print(i[0], end = " ")
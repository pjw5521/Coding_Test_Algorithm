# 페이지 178쪽
# 기본 정렬 라이브러리 사용
n = int(input())

data = []
for _ in range(n):
  data.append(int(input()))

data.sort()
data.reverse()

print(*data)
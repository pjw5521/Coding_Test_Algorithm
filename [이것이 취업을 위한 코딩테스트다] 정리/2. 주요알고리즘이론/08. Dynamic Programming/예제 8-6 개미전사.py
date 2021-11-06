# 페이지 220쪽 
n = int(input())

data = list(map(int,input().split()))

d = [0] * 100

d[0] = data[0]
d[1] = max(data[0], data[1])
for i in range(2, n):
  # 현재에서 -1 위치에 있는 식량을 먹거나, 현재 위치 식량과 현재에서 -2 위치에 있는 식량을 먹는다. 그 중에서 큰 것. 
  d[i] = max(d[i-1], d[i-2] + data[i])


print(d[n-1])
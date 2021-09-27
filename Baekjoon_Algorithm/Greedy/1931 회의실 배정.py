n = int(input())

data = []
for i in range(n):
  start, end = map(int, input().split())
  data.append([start ,end])

data.sort(key=lambda x:(x[1],x[0]))
# key 값을 기준으로 오름차순 
# 끝나는 시간이 빠른 순으로, 같으면 시작시간이 빠른 순으로
count = 1
end = data[0][1]

for i in range(1,n):
  # 시작시간이 끝나는 시간보다 크거나 같으면
  if (data[i][0] >= end):
    end = data[i][1]
    count += 1

print(count)
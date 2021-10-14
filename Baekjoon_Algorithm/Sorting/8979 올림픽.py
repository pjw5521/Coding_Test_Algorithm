# 문제 https://www.acmicpc.net/problem/8979
n, k  = map(int,input().split())

data = []

for _ in range(n):
  data.append(list(map(int,input().split())))

# 금, 은, 동 순서로 내림차순 정렬
data.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)

# 등수와 등수가 같은 개수를 저장할 변수
grade, s = 1, 0
for i in range(n):
  if i != 0:
    if data[i-1][1:] == data[i][1:]:
      s += 1
    else:
      if s:
        grade += s
        s = 0
      else:
        grade +=1 

  if data[i][0] == k:
    print(grade)
    break
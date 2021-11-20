import sys

input = sys.stdin.readline
test_num = int(input())

# 서류 1등은 무조건 뽑힘 
# 2등부터 면접 높은 순위랑 면접 순위 비교 
for j in range(test_num):
  n = int(input())
  d = []
  for k in range(n):
    d.append(list(map(int,input().split())))
    #a, b = map(int, input().split())
    #d[j].append([a,b])
  d.sort(key=lambda x :x[0])
  score = d[0][1]
  count = 1
  for k in range(1,n):
    if( score > d[k][1]):
      count += 1 
      score = d[k][1]
  print(count)
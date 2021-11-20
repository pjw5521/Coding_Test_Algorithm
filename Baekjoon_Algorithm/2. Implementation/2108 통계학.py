from collections import Counter
import sys

n  = int(sys.stdin.readline())

data = []
for _ in range(n):
  data.append(int(sys.stdin.readline()))

# round(변수, 소수점 아래 개수)
print(round(sum(data)/n))

# 오름차순 정렬
# sort() 후 reverse() 내림차순 정렬
data.sort()
index = n//2
print(data[index])

# 최빈값과 몇번 등장했는지
most = Counter(data).most_common()
if(len(most)> 1 and most[0][1] == most[1][1]):
  print(most[1][0])
else:
  print(most[0][0])

print(max(data)- min(data))
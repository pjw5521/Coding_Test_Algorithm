# 문제 332쪽
# https://www.acmicpc.net/problem/15686
from itertools import combinations 

INF = int(1e9)

n, m = map(int, input().split())

home = []
chicken = []

for i in range(n):
  a = list(map(int, input().split()))
  for j in range(n):
    # 집인 경우 위치 정보 저장
    if a[j] == 1:
      home.append((i,j))
    # 치킨집 인 경우 위치 정보 저장 
    elif a[j] == 2 :
      chicken.append((i,j)) 

# 치킨 집 중에서 m개 선택하는 조합 
candidate = list(combinations(chicken,m))

def simulate(candidate):
  result = 0
  for hx, hy in home:
    temp = INF
    for cx, cy in candidate :
      temp= min(temp, abs(hx- cx) + abs(hy-cy))
    result += temp

  return result 

result = INF
for i in candidate :
# 어떤 치킨 집의 조합이 가장 최솟값을 갖는지 
  result = min(result, simulate(i))
  
print(result)
# 문제 https://www.acmicpc.net/problem/1654
# 두번 품 
import sys
sys.setrecursionlimit(10000)
r =  sys.stdin.readline
k, n = map(int,r().split())

data = []
for _ in range(k):
  data.append(int(r()))

# start를 1로 설정해야 런타임 에러 안남 
start = 1
end = max(data)

while start <= end :
  mid = (start+end)//2
  total = 0 
  for i in data:
    # 얻을 수 있는 랜선 개수 
    total += i // mid

  if total >= n :
    start = mid + 1
  else:
    end = mid - 1 

print(end)
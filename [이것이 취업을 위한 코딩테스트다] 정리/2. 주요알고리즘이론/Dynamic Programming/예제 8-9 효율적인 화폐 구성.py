# 페이지 226쪽 
n,m = map(int,input().split())

data = []
for i in range(n):
  data.append(int(input()))

# 금액 i를 만들 수 있는 최소 화폐 개수 저장 
# 만들 수 없으면 10001 
d = [10001] * (m+1)

# 0원의 경우
d[0] = 0. 

# a(i) = min(a(i), a(i-k) + 1)
# k는 화폐의 단위 
for i in range(n):
  for j in range(data[i], m+1):
    if d[j-data[i]] != 10001 :
      d[j] = min(d[j],d[j-data[i]]+1)
  
if d[m] == 10001:
  print(-1)
else:
  print(d[m]) 
# https://www.acmicpc.net/problem/12865
# 물품 수, 최대 무게 
n, k = map(int,input().split())

# 배낭의 무게와 가치 
product = [[0,0]]

# dp[n][k] : n번째 물건까지 살펴보았을 때, 무게가 k인 배낭의 최대 가치 
dp = [ [0] * (k+1) for _ in range(n+1)]

for _ in range(n):
  product.append(list(map(int,input().split())))

for i in range(1, n+1):
  for j in range(1, k+1):
    # 현재 물건의 무게
    w = product[i][0]
    # 현재 물건의 가치 
    v = product[i][1]

    # 현재 물건의 무게가 현재 배낭의 허용 무게보다 크면 
    if j < w :
        # 현재 물건 선택하지 않음 
      dp[i][j] = dp[i-1][j]
    else:
       # 현재 넣을 물건의 무게만큼 배낭에서 뺀 후, 현재 넣을 물건 넣기 vs 현재 물건을 넣지 않고 현재 배낭 그대로 가져가기 
      dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

print(dp[n][k])
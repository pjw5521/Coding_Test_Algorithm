#https://www.acmicpc.net/problem/11053
n = int(input())

data = list(map(int,input().split()))

# data[i]를 마지막 원소로 가질 때 가장 긴 증가하는 부분 수열의 길이 
# 최솟값인 1로 초기화 
dp = [1] * n

for i in range(n):
# 본인의 왼쪽 숫자들 비교 
  for j in range(i):
  # 이전의 원소가 작은지 확인하여, 작다면 dp 최댓값 구해 +1 
    if data[j] < data[i]:
      dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
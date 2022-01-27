# https://www.acmicpc.net/problem/9251
a = list(str(input()))
b = list(str(input()))

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

answer = 0 

for i in range(len(a)):
  for j in range(len(b)):
    # 문자가 같으면 대각선 왼쪽의 값 
    if a[i] == b[j]:
      dp[j+1][i+1] = dp[j][i] + 1 
      answer = max(answer, dp[j+1][i+1])
    # 문자가 다르면 왼쪽이나 위쪽 중 큰 값 
    else :
      dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])

print(answer)
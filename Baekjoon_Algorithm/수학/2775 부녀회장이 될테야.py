# https://www.acmicpc.net/problem/2775
test = int(input())

for _ in range(test):
  k = int(input())
  n = int(input())
  
  # 0층부터 k층까지 있고 각 층마다 n호 
  num = [ [0] * n for _ in range(k+1)]

  # 1호부터 시작하고 0층의 경우 i호에 i명 거주 
  for i in range(n):
    num[0][i] = i + 1 
  
  # 1층부터 k층까지 
  for i in range(1, k+1):
    # 층별 각 호마다 반복 
    for j in range(n):
      # 1호면 전 층의 1호 사람 수
      if j == 0:
        num[i][j] = num[i-1][0]
      # 1호가 아니면 전 호수의 사람 수 + 전 층의 해당 호수 사람 수 
      else :
        num[i][j] = num[i][j-1] + num[i-1][j]

  print(num[k][n-1])
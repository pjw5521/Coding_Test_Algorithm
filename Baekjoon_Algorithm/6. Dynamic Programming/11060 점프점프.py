# https://www.acmicpc.net/problem/11060
# bfs 문제가 아니고 다이나믹 프로그래밍 문제 ! import sys
input = sys.stdin.readline 

n = int(input())

graph = list(map(int,input().split()))

dp = [n+1] * n
dp[0] = 0

for i in range(n):
  for j in range(1, graph[i]+1):
    if i+j >= n:
      break
    dp[i+j] = min(dp[i+j],dp[i]+1)

print(dp[n-1] if dp[n-1] != n+1 else -1)
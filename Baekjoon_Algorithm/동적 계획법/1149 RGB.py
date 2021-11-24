#https://www.acmicpc.net/problem/1149
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

# 만약 현재 빨간색이면, 이전, 초록과 파란색 비용 중 작은 비용으로 선택 
for i in range(1,n):
  data[i][0] = min(data[i-1][1], data[i-1][2]) + data[i][0]
  data[i][1] = min(data[i-1][0], data[i-1][2]) + data[i][1]
  data[i][2] = min(data[i-1][1], data[i-1][0]) + data[i][2]

print(min(data[n-1]))
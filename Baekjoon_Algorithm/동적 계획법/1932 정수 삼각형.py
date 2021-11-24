# https://www.acmicpc.net/problem/1932
'''
 삼각형의 꼭대기부터 내려오면서 최대 값을 저장 
 결국 삼각형의 가장 밑에는 해당 값까지 오기 위한 최대 값이 저장되고 
 max를 사용해 가장 큰 값 출력 
'''
import sys
input = sys.stdin.readline

n =int(input())

data = [] 

for _ in range(n):
  data.append(list(map(int,input().split())))

for i in range(1,n):
  for j in range(len(data[i])):
    # 맨 왼쪽 값일 때 
    if j == 0:
      data[i][j] = data[i-1][j] + data[i][j]
    # 맨 오른쪽 값일 때 
    elif j == len(data[i])-1:
      data[i][j] = data[i-1][j-1] + data[i][j]
    else:
      # 중간 값일 때 더 큰값과 더함 
      data[i][j] = max(data[i-1][j], data[i-1][j-1]) + data[i][j]
    
print(max(data[n-1]))
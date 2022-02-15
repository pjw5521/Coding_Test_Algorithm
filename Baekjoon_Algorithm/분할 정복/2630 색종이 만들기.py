# https://www.acmicpc.net/problem/2630
# 분할 정복

# 흰색 색종이 개수
count0 = 0
# 파란 색종이 개수 
count1 = 0

def sol(x, y, n):
  global count0
  global count1
  
  color = graph[x][y]
  
  for i in range(x, x+n):
    for j in range(y, y+n):
      # 처음 시작한 색과 다르면 
      if color != graph[i][j]:
        # 4등분하여 재귀적으로 호출 
        sol(x, y, n//2)
        sol(x+n//2 , y , n//2)
        sol(x, y +n//2 , n//2)
        sol(x+n//2, y+n//2, n//2)
        return
  # 흰색 색종이 개수 + 1 
  if color == 0:
    count0 += 1 
  # 파란 색종이 개수 + 1
  else:
    count1 += 1 
    
n = int(input())

graph = []

for _ in range(n):
  graph.append(list(map(int,input().split())))

sol(0,0,n)
print(count0)
print(count1)
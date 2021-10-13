import sys
sys.setrecursionlimit(100000) # 이거 안해주면 런타임 에러

m, n, k = map(int, input().split())

data = [ [0]*n for _ in range(m)] # 2차원 리스트

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

for _ in range(k):
  ax, ay, bx, by = map(int,input().split())
  for i in range(ay,by):
    for j in range(ax,bx):
      data[i][j] = 1

def dfs(y, x, area): 
# 넓이 넘겨주기 
  data[y][x] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if ( 0 <= nx < n) and ( 0 <= ny < m) and data[ny][nx] == 0: 
      area = dfs(ny, nx, area + 1)
  return area

count = []
for i in range(m):
  for j in range(n):
    if data[i][j]== 0:
    # 리스트의 길이가 영역 개수 
    # 리스트에 담긴 수는 넓이 
      count.append(dfs(i,j,1))

print(len(count))
count.sort()
print(*count) # 배열 앞에 * 붙여서 출력하면 인자를 하나씩 넘겨주는 효과 [] 없이 출력 가능
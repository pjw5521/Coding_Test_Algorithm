n, m= map(int,input().split())

data = []
for _ in range(n):
  data.append(list(map(int, input())))

# 띄어쓰기 없이 넣을 때는 split() 없어야 함. 
def dfs(x,y):
  if x <= -1 or x >=n or y >= m or y <= -1:
    return False
  if data[x][y] == 0 :
    data[x][y] = 1
    dfs(x-1,y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

count = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      count += 1

print(count)
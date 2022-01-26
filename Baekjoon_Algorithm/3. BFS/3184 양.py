#https://www.acmicpc.net/problem/3184
from collections import deque

nx = [ 1, -1, 0, 0 ]
ny = [ 0, 0, 1, -1 ]

def bfs(i,j):
  # 울타리로 둘러쌓인 공간에 있는 늑대와 양의 수 계산 
  v_num = 0
  c_num = 0 
  q = deque()
  q.append((i,j))
  maps[i][j] = "."

  while q :
    x, y = q.popleft()

    for i in range(4):
      dx = x + nx[i]
      dy = y + ny[i]
      # 울타리가 아니면 
      if 0 <= dx < r and 0 <= dy < c and maps[dx][dy] != "#":
      # 큐에 추가 
        q.append((dx,dy))
        # 늑대 수 증가 & 탐색한 부분 울타리로 바꿔주기 
        if maps[dx][dy] == "v":
          v_num += 1 
          maps[dx][dy] = "#"
		# 양의 수 증가 
        elif maps[dx][dy] == "o":
          c_num +=1 
          maps[dx][dy] = "#"
        else: 
          maps[dx][dy] = "#"

  return v_num, c_num

r, c = map(int,input().split())

maps=[]

for _ in range(r):
  maps.append(list(map(str,input())))

# 살아남은 늑대와 양의 수 저장 
v_result = 0
o_result = 0 

for i in range(r):
  for j in range(c):
    if maps[i][j] == 'v' :
      v_num, o_num = bfs(i,j)
      # 시작 위치의 늑대 수 포함 
      v_num += 1 
      # 늑대의 수가 양의 수보다 크거나 같으면 살아남은 늑대 수 증가 
      if v_num >= o_num:
        v_result += v_num
      # 양의 수가 더 많으면 살아남은 양의 수 증가 
      else:
        o_result += o_num
    elif maps[i][j]== 'o':
      v_num, o_num = bfs(i,j)
      # 시작 위치의 양의 수 포함 
      o_num += 1 
      if v_num >= o_num:
        v_result += v_num
      else:
        o_result += o_num

print(o_result, v_result)

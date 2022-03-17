# https://www.acmicpc.net/problem/1913
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

graph = [ [0] * n  for _ in range(n) ]
x = n // 2
y = n // 2
num = 1
graph[x][y] = num
len = 0 
answer = []
    
if m == 1 :
    answer.append(x+1)
    answer.append(y+1)
    
while True:
    for i in range(4):
        for _ in range(len):
            x += dx[i]
            y += dy[i]
            num += 1 
            graph[x][y] = num
            if num == m:
                answer.append(x+1)
                answer.append(y+1)            
            
    if x == y == 0:
        break
    x -= 1
    y -= 1
    len += 2
    
for i in graph:
    print(*i)
print(*answer)
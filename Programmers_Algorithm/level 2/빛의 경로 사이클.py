# https://programmers.co.kr/learn/courses/30/lessons/86052
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solution(grid):
    global visited, n, m 
    answer = []
    n = len(grid)
    m = len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k] :
                    cost= simul(i,j,k,grid)
                    if cost != 0:
                        answer.append(cost)
    answer.sort()    
    return answer
    
def simul(x, y, d, grid):
    global visited 
    nx, ny, nd = x, y, d 
    visited[x][y][d] = True 
    cnt = 0 
    while True :
        nx = (nx + dx[nd]) % n 
        ny = (ny + dy[nd]) % m 
        cnt += 1 
        if grid[nx][ny] == 'R':
            nd = (nd+1) % 4 
        elif grid[nx][ny] == 'L':
            nd = (nd-1) % 4
        if visited[nx][ny][nd]:
            if x == nx and y == ny and d == nd:
                return cnt 
            else:
                return 0 
        visited[nx][ny][nd] = True 
        
g = ["SL","LR"]
print(solution(g))
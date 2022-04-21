# https://programmers.co.kr/learn/courses/30/lessons/72415
from collections import defaultdict, deque
from itertools import permutations 
import copy 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 컨트롤 누르고 이동할 때 
def ctrl_move(board, x, y, mx, my):
    cx, cy = x, y
    
    while True :
        # 한 방향으로 계속 이동 
        nx = cx + mx
        ny = cy + my
        # 범위에서 벗어나면 중단 
        if not ( 0<= nx < 4 and 0 <= ny < 4):
            return cx, cy
        # 다른 카드를 만나면 중단 
        if board[nx][ny] != 0:
            return nx, ny
        cx = nx
        cy = ny 
        
# 그냥 위, 아래, 왼쪽, 오른쪽 한 칸씩 이동할 때 
def bfs(board, start, end):
	# 현재 위치
    x, y = start
    # 이동할 위치 
    find_x, find_y = end 
    
    q = deque()
    # 위치 인덱스와 이동 횟수 큐에 삽입 
    q.append((x,y,0))
    # 방문 표시할 배열 
    visited = [ [0]* 4 for _ in range(4) ]
    
    while q:
        x, y, cnt = q.popleft()
        
        # 같은 번호인 카드 위치로 왔으면 이동 횟수 return 
        if x == find_x and y == find_y:
            return cnt 
            
        # 위, 아래, 왼쪽, 오른쪽에 대하여 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나지 않았고, 방문하지 않았으면 
            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny] :
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = 1
            
            # 컨트롤 누르고 이동할 때 위치 
            cx, cy = ctrl_move(board, x, y, dx[i], dy[i])
            q.append((cx, cy, cnt +1))  
    
    return -1 
    
def solution(board, r, c):
    answer = int(1e9)
    
    dict = defaultdict(list)
    
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 :
            	# 카드 번호 key, 위치가 value 
                dict[board[i][j]].append((i,j))
              
    # 카드 번호 선택하는 순서 
    permute = list(permutations([i+1 for i in range(len(dict))], len(dict)))

    for i in permute :
        tmp_board = copy.deepcopy(board)
        cnt = 0 
        x, y = r, c 
        
        for j in i:
            # 현재 위치에서 같은 번호인 두 카드까지 위치 
            choice1 = bfs(tmp_board, (x,y), dict[j][0])
            choice2 = bfs(tmp_board, (x,y), dict[j][1])
            
            # 더 가까운 카드로 이동 
            if choice1  < choice2:
                cnt += choice1 
                # 같은 번호인 다른 카드까지 거리 
                cnt += bfs(tmp_board, dict[j][0], dict[j][1])
                # 현재 위치 갱신 
                x,y = dict[j][1]
            else :
                cnt += choice2
                # 같은 번호인 다른 카드까지 거리 
                cnt += bfs(tmp_board, dict[j][1], dict[j][0])
                # 현재 위치 갱신 
                x,y = dict[j][0]
                
            # 카드 지우기 
            tmp_board[dict[j][0][0]][dict[j][0][1]] = 0 
            tmp_board[dict[j][1][0]][dict[j][1][1]] = 0
            # 카드 선택 비용 
            cnt += 2
            
        # 최솟값 갱신 
        answer = min(answer, cnt)
    return answer
    
b = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1
print(solution(b,r,c))
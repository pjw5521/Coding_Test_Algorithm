# https://www.acmicpc.net/problem/2448
n = int(input())

graph = [ [" "] * 2*n for _ in range(n) ]

def draw(x, y, n):
    # 3일 때 삼각형 그리기 
    if n == 3 :
     	# 첫째줄 
        graph[x][y] = '*'
        # 둘째줄 
        graph[x+1][y-1] = graph[x+1][y+1] = '*'
        # 셋째줄 
        for i in range(-2, 3):
            graph[x+2][y+i] = "*"
    # 삼등분 
    else:
        size = n // 2 
        draw(x, y, size)
        draw(x+size,y-size,size)
        draw(x+size,y+size,size)

draw(0, n-1, n)

for i in graph:
    print("".join(i))
        





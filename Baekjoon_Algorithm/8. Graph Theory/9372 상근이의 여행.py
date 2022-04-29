# https://www.acmicpc.net/problem/9372
import sys
input = sys.stdin.readline 

# 같은 집합에 속하는지 판별 
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        
    return parent[x]
    
# 같은 집합으로 합치기 
def union(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return 
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    
    # 부모 저장 테이블 
    parent = [0] * (n+1)
    
    for i in range(1,n+1):
        parent[i] = i 
        
    edges = []
    
    # 간선들 정보 저장 
    for _ in range(m):
        a, b = map(int,input().split())
        edges.append((a,b))
        edges.append((b,a))
    
    # 비행기 개수 
    result = 0 
    for edge in edges :
        a,b = edge
        # 같은 집합에 속하지 않으면 
        if find(a) != find(b):
        	# 합치기 
            union(a,b)
            # 비행기 개수 증가 
            result +=1 

    print(result)
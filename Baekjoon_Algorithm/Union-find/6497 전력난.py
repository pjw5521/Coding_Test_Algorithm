# https://www.acmicpc.net/problem/6497
import sys
input = sys.stdin.readline 

# 부모 찾는 함수 
def find(x):
    if x == parent[x]:
        return x 
    parent[x] = find(parent[x])
    
    return parent[x]
   
# 합집합 함수 
def union(a,b):
    a = parent[a]
    b = parent[b]
    
    if a == b:
        return 
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
while True:
    m, n = map(int,input().split())
    
    # 중단 조건 
    if m == 0 and n == 0 :
        break 

	# 부모 저장 테이블 
    parent = [0] * m 
    
    for i in range(1,m):
        parent[i] = i 
        
    edges = []
    answer = 0 
    for _ in range(n):
        a, b, c = map(int,input().split())
        edges.append((c, a, b))
        edges.append((c, b, a))
        # 전체 가로등의 비용구하기 
        answer += c
        
    edges.sort()
    for edge in edges:
        cost, a, b = edge
    
        if find(a) != find(b):
            union(a,b)
            # 설치할 가로등 비용 빼기 
            answer -= cost 
            
    # 절약한 가로등 비용     
    print(answer)
    
                
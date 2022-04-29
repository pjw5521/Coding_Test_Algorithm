# https://www.acmicpc.net/problem/1197
# 같은 집합에 속하는지 판별 
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
    
# 두 집합 합치기 
def union(x, y):
    x= find(x)
    y = find(y)
    
    if x == y:
        return 
        
    if x < y:
        parent[y] =x 
    else:
        parent[x] = y
        
v, e = map(int,input().split())

# 부모 노드 저장 테이블 
parent = [0] * (v+1)
for i in range(1,v+1):
    parent[i] = i 
    
edges = []

# 간선 정보 
for _ in range(e):
    a, b, c = map(int,input().split())
    edges.append((c,a,b))
    edges.append((c,b,a))
    
# 비용 기준으로 정렬 
edges.sort()

result = 0 
for edge in edges:
    cost, a, b = edge
    # 같은 집합에 속하지 않으면 
    if find(a) != find(b):
    	# 합치기
        union(a,b)
        # 비용 더하기 
        result += cost

print(result)
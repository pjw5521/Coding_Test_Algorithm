# https://www.acmicpc.net/problem/1647
import sys
input = sys.stdin.readline 

# 부모 찾는 함수 
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    
    return parent[x]

# 두 집합 합치는 함수 
def union(a,b):
    a = parent[a]
    b = parent[b]
    
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int,input().split())

# 부모 저장 테이블 
parent = [0] * (n+1)

# 자기 자신으로 초기화 
for i in range(1,n+1):
    parent[i] = i 
    
edges = []
for _ in range(m):
    a, b, cost = map(int,input().split())
    edges.append([cost,a,b])

# cost 기준 정렬 
edges.sort()
# 연결 비용 저장
answer = []

for edge in edges:
    cost, a, b = edge
    
    # 같은 집합에 속하지 않으면 
    if find(a) != find(b):
    	# 연결하고 비용 더하기 
        union(a,b)
        answer.append(cost)
    
 # 가장 큰 비용 제거 
print(sum(answer[:-1]))
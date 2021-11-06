# 문제 300쪽
# 크루스칼 알고리즘으로 최소 신장 트리를 찾은 후 가장 비용이 큰 간선 제거 
def find_parent(parent,x):
    # 루트 노드가 아니면 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기, 루트 노드가 작은 걸로 루트 노드 변경 
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b


# 노드의 개수와 간선의 개수 
v,e  = map(int,input().split())

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수 
edges = []
result = 0 

# 부모 테이블 초기화
parent = [0] * (v+1)

# 부모 노드를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
  a,b,cost = map(int,input().split())
  edges.append((cost,a,b))

# 비용 순으로 정렬 
edges.sort()
last = 0
for edge in edges:
  cost, a, b = edge 
  # 사이클 발생하지 않으면 union 연산 수행 
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    last = cost 

print(result - last)


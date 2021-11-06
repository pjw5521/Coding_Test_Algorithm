# 문제 273쪽 

def find_parent(parent,x):
    # 루트 노드가 아니면 재귀적으로 호출
    if parent[x] != x :
        return find_parent(parent,parent[x])
    return x 

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

# 부모 테이블 초기화
parent = [0] * (v+1)

# 부모 노드를 자기 자신으로 초기화
for i in range(v+1):
    parent[i] = i

cycle = False

# 원소 합치기 
for i in range(e):
    a, b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else :
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생했습니다 ")
else :
    print("사이클이 발생하지 않았습니다. ")

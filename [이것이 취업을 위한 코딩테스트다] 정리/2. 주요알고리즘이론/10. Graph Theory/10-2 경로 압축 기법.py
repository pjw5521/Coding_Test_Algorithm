# 페이지 275쪽 

# 최대 O(v) 시간 소요 가능 
def find_parent(parent,x):
    # 루트 노드가 아니면 재귀적으로 호출
    if parent[x] != x :
        return find_parent(parent,parent[x])
    return x 

# 개선
def find_parent(parent,x):
    # 루트 노드가 아니면 재귀적으로 호출
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
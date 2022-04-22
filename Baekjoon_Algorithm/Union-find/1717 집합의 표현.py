# https://www.acmicpc.net/problem/1717
# Union-Find 알고리즘 
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline 

def find(a):
    if a == parent[a]:
        return a
    # 루트 노드 찾기 
    p = find(parent[a])
    # 루트 노드 갱신 
    parent[a] = p 
    return parent[a]
    
def union(a,b):
    # 루트 노드 찾기 
    a = find(a)
    b = find(b)
    
    # 두 루트 노드가 같다면 동일한 집합 
    if a == b:
        return
    # 두 집합 합치기  
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
n, m = map(int,input().split())

# 부모 테이블 
parent = [0] * (n+1)

# 자기 자신을 설정 
for i in range(1,n+1):
    parent[i] = i 
    
for _ in range(m):
    cal, a, b = map(int,input().split())
    
    # 합치기 
    if cal == 0:
        union(a,b)
    else:
        # 같은 집합인지 확인하기 
        if find(a) == find(b):
            print('YES')
        else:
            print("NO")
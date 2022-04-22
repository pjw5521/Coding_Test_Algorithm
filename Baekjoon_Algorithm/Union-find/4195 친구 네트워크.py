# https://www.acmicpc.net/problem/4195
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y]
        
t = int(input())

for _ in range(t):
    f = int(input())
    
    # 부모 저장 
    parent = dict()
    # 네트워크에 몇 명 있는지 저장 
    number = dict()
    
    for i in range(f):
        x, y = map(str, input().split())
        
        # 자기 자신으로 초기화 
        if x not in parent:
            parent[x] = x 
            number[x] = 1
        
        if y not in parent:
            parent[y] = y
            number[y] = 1 
        
        union(x,y)
        
        print(number[find(x)])
        
        
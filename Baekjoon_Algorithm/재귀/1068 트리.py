# https://www.acmicpc.net/problem/1068

def delete(node):
    # 지워진 함수는 -2로 표시 
    parent[node] = -2
    for i in range(n):
    	# 지운 노드를 부모로 가지는 노드들도 함께 재귀적으로 삭제해주기 
        if parent[i] == node :
            delete(i)

n = int(input())

parent = list(map(int,input().split()))

node = int(input())

delete(node)
ans = 0 
for i in range(n):
	# 지워지지 않았고 자신을 부모로 가지는 노드들이 없으면 
    if parent[i] != -2 and i not in parent :
        ans += 1 
        
print(ans)
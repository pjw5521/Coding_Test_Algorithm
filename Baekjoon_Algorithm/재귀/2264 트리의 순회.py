# https://www.acmicpc.net/problem/2263
# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(10 **5)
input = sys.stdin.readline 

n = int(input())

inorder = list(map(int,input().split()))
post = list(map(int,input().split()))

index = [0] * (n+1)

# 정점의 인덱스 저장 -> 왼쪽 서브 트리 노드 수, 오른쪽 서브 트리 노드 수 알 수 있음 
for i in range(n):
    index[inorder[i]] = i 

def preorder(istart,iend,pstart,pend):
    # 역전 시 중단 
    if istart > iend or pstart > pend:
        return 
    # 후위 순회의 맨 마지막 정점은 전위 순회의 처음 정점 
    root = post[pend]
    # 전위 순회이므로 정점 출력 먼저 
    print(root, end = " ")
    
    # 왼쪽 서브 트리 
    left = index[root] - istart
    # 오른쪽 서브 트리
    right = iend - index[root]
    
    # 중위순회, 후위 순회의 왼쪽 서브 트리
    preorder(istart, istart + left -1 , pstart, pstart + left -1)
    # 중위순회, 후위 순회의 오른쪽 서브 트리
    preorder(iend - right +1, iend, pend-right, pend-1)
    
preorder(0,n-1,0,n-1)
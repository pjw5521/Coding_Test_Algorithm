# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10 **6)
input = sys.stdin.readline 

def sol(start,end):
    # 역전 시 중단 
    if start > end :
        return 
    # 루트노드
    root = tree[start]
    index = start + 1 
    
    while index <= end: 
        # 루트보다 큰 숫자가 나오면 오른쪽 서브 트리의 루트라는 뜻 
        if tree[index] > root :
            break
        index += 1 
        
    # 왼쪽 서브 트리   
    sol(start + 1, index -1)
    # 오른쪽 서브 트리
    sol(index,end)
    # 후위순회이므로 마지막에 출력 
    print(root)

tree= []

# 입력 중단 조건이 없으므로 예외 발생 시 중단하도록 
while True:
    try :
        tree.append((int(input())))
    # 예외 발생 시 break
    except :
        break
    
sol(0,len(tree)-1)
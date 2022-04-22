# https://www.acmicpc.net/problem/1976
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

def find(a):
    if a != parent[a]:
        p = find(parent[a])
        parent[a] = p
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
m = int(input())

graph = []

parent = [0] * n

for i in range(n):
    parent[i] = i
    
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 1 :
            union(i,j)
    
# 경로 체크
parents = [-1] + parent
path = list(map(int,input().split()))
start = parents[path[0]]
for i in range(1,m):
    if parents[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
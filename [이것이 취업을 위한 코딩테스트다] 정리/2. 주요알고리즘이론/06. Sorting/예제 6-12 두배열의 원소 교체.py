# 문제 182쪽
n, k = map(int, input().split())

A= list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
B.reverse()
for i in range(k):
  if A[i] < B[i]:
    A[i],B[i] = B[i],A[i]
  else:
    break

print(sum(A))
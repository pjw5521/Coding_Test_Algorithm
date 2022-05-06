# https://www.acmicpc.net/problem/1057
n, a, b = map(int,input().split())

cnt = 0 
# 토너먼트 규칙 사용 
while a!= b:
    a -= a // 2 
    b -= b // 2 
    cnt += 1 
    
print(cnt)
# https://www.acmicpc.net/problem/1208
# 투 포인터 예제 
n, m = map(int,input().split())

data = list(map(int,input().split()))

start, end = 0, 1 
cnt = 0 

while start <= end and end <= n :
    sum_num = sum(data[start:end])
    
    if sum_num == m:
        cnt += 1 
        start += 1
    
    # 부분합 배열의 크기 증가 
    elif sum_num < m:
        end +=1 
    # 부분합 배열의 크기 감소 
    else :
        start += 1 
    
print(cnt)
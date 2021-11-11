# https://www.acmicpc.net/problem/6236

n, m = map(int,input().split())

data = []
for _ in range(n):
    data.append(int(input()))

start = min(data)
end = sum(data)

while start <= end :
    mid = ( start + end ) // 2
    result = mid 
    num = 1 
    for i in data:
        
        if i <= result :
            result -= i
        else:
            num += 1 
            result = mid
            result -= i

    # 인출한 수가 더 많거나, 해당 금액으로 살 수 없을 때 
    if num > m or mid < max(data):
        start = mid + 1 
    else :
        end = mid -1 
        k = mid 

print(k)
               
        
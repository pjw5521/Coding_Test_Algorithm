#완전 탐색 유형으로 분류되기도 함 
n = int(input())
count =0
for i in range(n+1):
    for k in range(60):
        for j in range(60):
            if '3' in str(i)+str(k)+str(j):
                count +=1

print(count)

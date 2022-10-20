# 재귀 
def fibo(x):
    if x == 0 :
        return x 
    if x == 1 or x == 2 :
        return 1
    else :
        return fibo(x-1) + fibo(x-2)

# 반복문 
dp = [0] * 100

dp[1] = 1 
dp[2] = 1 
n = 99 
for i in range(3,n-1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
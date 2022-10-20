# 에라토스테네스의 채로 소수 판별 
def is_prime(n):
    for i in range(1, int(i**0.5)+1):
        if n % i == 0:
            return False 
    
    return True 
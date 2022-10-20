# 재귀를 이용한 팩토리얼 
def factorial(x):
    if x == 1 :
        return x 
    return x * factorial(x)
    
# 내장 함수 이용 
import math
n = int(input())
math.factorial(n)
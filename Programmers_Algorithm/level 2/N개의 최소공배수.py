# https://programmers.co.kr/learn/courses/30/lessons/12953
from collections import deque 

# 최대공약수 구하기
def gcd(x,y):
    while y:
        x, y = y, x%y
    return x 
    
# 최소공배수 구하기 
def lcm(x,y):
    return (x*y) // gcd(x,y)
    
def solution(arr):
    
    q = deque(arr)
    
    # 큐에 하나 남을 때까지 반복 
    while len(q) > 1 :
    	# 두 개씩 빼서 두 수의 최소 공배수 구하고 다시 넣어주기 
        x = q.popleft()
        y = q.popleft()
        
        q.append(lcm(x,y))
        
    return q.pop()
    
arr = [1,2,3]
print(solution(arr))
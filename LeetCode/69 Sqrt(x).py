# https://leetcode.com/problems/sqrtx/

# operator 사용 불가 
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
    
# 이진 탐색 사용 
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x 
        
        # 등호 반드시
        while start <= end :
            mid = (start+end) // 2 
            
            tmp = mid * mid 
            
            if tmp == x :
                return mid 
            
            if tmp < x :
                start = mid + 1 
            else :
                end = mid - 1 
            
        return end 
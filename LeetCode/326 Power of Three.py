# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # 3^31을 N으로 나눈 나머지가 0 이면 
        if n > 0 and pow(3,31,n) == 0 :
            return True 
        
        return False 
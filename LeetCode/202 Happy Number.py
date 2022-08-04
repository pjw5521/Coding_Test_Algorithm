# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        num = n 
        
        # 순환 체크할 집합  
        visited = set()
    
        while num:
            # 무한 순환 
            if num in visited :
                return False 

            visited.add(num)
            tmp = 0 

            for i in str(num):
                tmp += int(i) * int(i)

            if tmp == 1 :
                return True 
            else :
                num = tmp     

        return False 
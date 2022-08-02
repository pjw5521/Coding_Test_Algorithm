# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x > 0 :
            ans =  int(str(x)[::-1])
        else :
            ans = -1 * int(str(x*-1)[::-1])
        
        if ans not in range (-2**31, 2**31):
            return 0
        
        return ans 
        
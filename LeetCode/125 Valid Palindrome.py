# https://leetcode.com/problems/valid-palindrome/
from collections import deque 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = deque()
        
        for i in s:
            # 영어,한글 또는 숫자 
            if i.isalnum():
                tmp.append(i.lower())
        
        while len(tmp) > 1 :
            if tmp.pop().upper() != tmp.popleft().upper():
                return False 
            
            
        return True
        
        
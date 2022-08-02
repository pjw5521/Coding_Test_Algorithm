# https://leetcode.com/problems/valid-parentheses/
from collections import deque 
class Solution:
    def isValid(self, s: str) -> bool:
        check = 0 
        q = deque()
        for i in range(len(s)):
            if check < 0 :
                return False 
                
            if s[i] in {'(', '[', '{'}:
               check += 1
               q.append(s[i])
            else :
                if not q:
                    return False 
                
                tmp = q.pop()
                check -= 1
                if s[i] == ')':
                    if tmp != '(':
                        return False 
                elif s[i] == '}':
                    if tmp != '{':
                        return False 
                else :
                    if tmp != '[':
                        return False 
                
        
        if check != 0 :
            return False
        else :
            return True 
            
solution= Solution()
print(solution.isValid('()'))
# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        
        for a, b in enumerate(s):
            if dic[b] == 1 :
                return a
            
        return -1 
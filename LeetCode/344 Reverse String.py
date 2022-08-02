# https://leetcode.com/problems/reverse-string/

# 파이썬 내장 함수 사용 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        """
        Do not return anything, modify s in-place instead.
        """
        
# 투포인터 사용 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0 
        right = len(s)-1
        
        while left <= right :
            s[left], s[right] = s[right], s[left]
            left += 1 
            right -= 1 
        """
        Do not return anything, modify s in-place instead.
        """
        
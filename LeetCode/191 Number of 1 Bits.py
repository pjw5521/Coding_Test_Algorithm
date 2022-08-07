# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # 이진수 문자열로 바꿔주는 함수 
        s = bin(n)
        return s.count('1')
# https://leetcode.com/problems/excel-sheet-column-number/

# 26진수로 보고 풀기 
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0 
        for a, b in enumerate(columnTitle[::-1]):
            # ord('A') == 65
            ans += (ord(b) - 64) * (26**a)
        return ans 
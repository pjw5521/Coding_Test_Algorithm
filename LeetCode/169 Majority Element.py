# https://leetcode.com/problems/majority-element/
from collections import defaultdict 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict = defaultdict(int)
        
        for i in nums:
            dict[i] += 1 
        
        cnt = 0
        ans = 0 
        for i in dict:
            if dict[i] > cnt :
                cnt = dict[i]
                ans = i

        return ans
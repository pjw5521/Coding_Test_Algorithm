# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = set([ i for i in range(max(nums))])
        
        nums = set(nums)
        
        differ = total - nums 
        
        if not differ :
            return max(nums) + 1 
        else :
            return differ.pop()
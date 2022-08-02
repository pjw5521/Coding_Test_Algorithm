# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 뒤에서부터 
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0 :
                nums.pop(i)
                nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
        
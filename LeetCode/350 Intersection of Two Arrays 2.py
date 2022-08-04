# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [] 
        
        # 숫자 key, 숫자의 개수 value 
        cnt = Counter(nums1)
        
        for i in nums2:
            if i in cnt and cnt[i] != 0 :
                cnt[i] -= 1 
                result.append(i)
                
        return result
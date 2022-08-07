# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        s = set()
        
        while head != None :
            if head not in s:
                s.add(head)
            else :
                return True 
            
            head = head.next
        
        return False 
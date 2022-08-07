# https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        tmp = []
        
        while head != None :
            tmp.append(head.val)
            head = head.next 
            
        if tmp == tmp[::-1]:
            return True 
        
        return False 
    
# deque 사용하면 시간 복잡도 줄어듬 
from collections import deque 
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 데이터 타입 deque로
        q = deque ()
            
        node = head 
        if not head:
            return True
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True
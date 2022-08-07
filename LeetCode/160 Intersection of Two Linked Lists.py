# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        h1 = headA
        h2 = headB
        
        # 같을 때까지 
        while h1 != h2 :
            # 끝까지 갔으면 반대쪽 출발 지점으로 보냄 -> 만약 같은 노드가 있다면 걸리게 되어있음  
            # 두 리스트를 같은 크기로 만들어주는 것 
            if not h1 :
                h1 = headB 
            else :
                h1 = h1.next
            
            if not h2 :
                h2= headA
            else :
                h2 = h2.next
            
        return h1 
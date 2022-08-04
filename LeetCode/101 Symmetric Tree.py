# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, root)])
        
        while q :
            # 왼쪽, 오른쪽 트리의 부모 
            left, right  = q.popleft()
            
            if not left and not right :
                continue 
                
            # 둘 중 하나 부모가 없다면 대칭이 아니라는 뜻 
            if not left or not right :
                return False 
            
            else :
                # 두 부모가 같으면 
                if left.val == right.val :
                    # 서로 대칭이어야 하므로 
                    
                    # 왼쪽 트리의 왼쪽과 오른쪽 트리의 오른쪽 
                    q.append((left.left, right.right))
                    # 왼쪽 트리의 오른쪽과 왼쪽 트리의 오른쪽 
                    q.append((left.right, right.left))
                else :
                    return False 
            
        return True 
        
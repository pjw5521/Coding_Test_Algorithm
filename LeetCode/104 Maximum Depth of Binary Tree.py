# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = 0 
        
    def dfs(self, node: TreeNode, depth):
        if not node :
            return 
        
        # 최대 깊이 갱신 
        if self.max_depth < depth :
            self.max_depth = depth 
        
        if node.left :
            self.dfs(node.left, depth+1)
        if node.right:
            self.dfs(node.right, depth + 1 )
                
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        self.dfs(root, 1)
                
        return self.max_depth
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 이진 탐색 트리 문제 
# 이진 탐색 트리 : 이진 트리는 자식 노드가 2개인 트리인데, 왼쪽 트리는 부모보다 작은 값, 오른쪽 트리는 부모보다 큰 값
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            if left > right :
                return 
            
            # 가운데 값이 root 
            mid = (left+right+1)//2 
            
            root = TreeNode(nums[mid])
            
            # 왼쪽 서브 트리
            root.left=dfs(left, mid-1)
            # 오른쪽 서브 트리 
            root.right = dfs(mid +1 , right)
            
            return root 
        
        return dfs(0 ,len(nums)-1)
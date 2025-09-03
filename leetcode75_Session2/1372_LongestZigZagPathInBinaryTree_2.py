# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        maxLength = 0
        def dfs(node, leftCount, rightCount):
            nonlocal maxLength
            if not node:
                return
            maxLength = max(maxLength, leftCount, rightCount)

            dfs(node.left, rightCount+1, 0)
            dfs(node.right, 0, leftCount+1)
        
        dfs(root, 0, 0)
        return maxLength
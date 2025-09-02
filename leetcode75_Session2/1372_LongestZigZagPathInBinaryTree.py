'''
Memorize this solution
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        max_length = 0
        
        def dfs(node, left, right):
            nonlocal max_length

            max_length = max(max_length, left, right)
            if node.left:
                dfs(node.left, right+1, 0)
            
            if node.right:
                dfs(node.right, 0, left+1)
        

        dfs(root, 0, 0)
        return max_length
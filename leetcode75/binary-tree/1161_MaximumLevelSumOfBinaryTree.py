# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = {}

        def dfs(node, depth):
            if not node:
                return node

            if depth not in d:
                d[depth] = 0
            
            d[depth] += node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            

        dfs(root, 0)
        max_sum = max(d.values())
        for depth, value in d.items():
            if value == max_sum:
                return depth+1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        if not root:
            return 0

        def dfs(node, prevLength):
            nonlocal maxDiameter


            left = right = 0
            if node.left:
                left = dfs(node.left, prevLength+1)
            
            if node.right:
                right = dfs(node.right, prevLength+1)
            
            maxDiameter = max(maxDiameter, prevLength, left + right)
            return max(left, right)+1

        dfs(root, 0)
        print(maxDiameter)
        return maxDiameter
            

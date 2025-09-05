# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if not node or node == p or node == q:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            # This traverses the new parent node to the top
            if left and right:
                return node
            
            # needs to return child nodes if 7 and 4 are using 
            return left or right

        return dfs(root, p, q)
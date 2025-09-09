# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        def dfs(node):
            if not node or node.val == val:
                return node

            if val < node.val:
                left = dfs(node.left)
                return left
            else:
                right = dfs(node.right)
                return right

        return dfs(root)
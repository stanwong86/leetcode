# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        if not root:
            return count

        def dfs(node, maxParent):
            nonlocal count

            if not node:
                return

            if node.val >= maxParent:
                count += 1

            maxParent = max(maxParent, node.val)

            dfs(node.left, maxParent)
            dfs(node.right, maxParent)

        dfs(root, -float('inf'))
        return count
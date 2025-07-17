# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaves(root):
            if not root:
                return []

            if not root.left and not root.right:
                return [root.val]
            
            leftLeaves = []
            rightLeaves = []

            leftLeaves.extend(getLeaves(root.left))
            rightLeaves.extend(getLeaves(root.right))

            leftLeaves.extend(rightLeaves)
            return leftLeaves
        

        left = getLeaves(root1)
        right = getLeaves(root2)
        return left == right
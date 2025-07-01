# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def countGoodNodes(curr, maxValue=None):
            if curr is None:
                return 0

            count = 0

            if maxValue is None or curr.val >= maxValue:
                count += 1
                maxValue = curr.val

            return count + countGoodNodes(curr.left, maxValue) + countGoodNodes(curr.right, maxValue)
        
        count = 1

        count = countGoodNodes(root)
        return count
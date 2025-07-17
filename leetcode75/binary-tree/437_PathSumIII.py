# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(curr, targetSum, parentVals):
            if curr is None:
                return 0
            count = 0
            currSum = curr.val
            if currSum == targetSum:
                count = 1

            for val in reversed(parentVals):
                currSum += val
                if currSum == targetSum:
                    count += 1
        
            leftVals = parentVals + [curr.val]
            rightVals = parentVals + [curr.val]
            
            leftCount = traverse(curr.left, targetSum, leftVals)
            rightCount = traverse(curr.right, targetSum, rightVals)
            return count + leftCount + rightCount

        return traverse(root, targetSum, [])
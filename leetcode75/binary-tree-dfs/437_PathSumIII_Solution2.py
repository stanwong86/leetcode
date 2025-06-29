'''
Solution2 is more optimal. Runs in O(N). Solution 1 is not great because it runs in O(N^2) because it needs
to look through all the elements.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currSum):
            if not node:
                return 0
            
            currSum += node.val
            count = existingSums[currSum - targetSum]
            existingSums[currSum] += 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            existingSums[currSum] -= 1
            return count


        existingSums = defaultdict(int)
        existingSums[0] = 1
        return dfs(root, 0)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevel = 0
        maxSum = -float('inf')
        sums = []

        queue = deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            currSum = 0
            for i in range(n):
                node = queue.popleft()
                if not node:
                    continue
                currSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            
            sums.append(currSum)
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = len(sums)

        return maxLevel
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
        currLevel = 1

        queue = deque()
        if root:
            queue.append(root)

        while queue:
            n = len(queue)

            currSum = 0
            for _ in range(n):
                node = queue.popleft()

                currSum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = currLevel
            
            currLevel += 1
        
        return maxLevel
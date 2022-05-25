class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def nodeDepth(root, level=0):
            if root is None:
                return level
            return max(nodeDepth(root.left, level+1), nodeDepth(root.right, level+1))
        return nodeDepth(root)


# vals = [3,9,20,None,None,15,7]
vals = [1,None,2]

root = dummy = TreeNode(vals[0])
i = 1
while i < len(vals):
    if i % 2 == 1:
        root.left = TreeNode(vals[i])
    else:
        root.right = TreeNode(vals[i])
        root = root.left
    i += 1

s = Solution()
maxDepth = s.maxDepth(dummy)
print(maxDepth)

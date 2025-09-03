# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append((0, root))
        while queue:
            index, node = queue.popleft()
            # print('len', len(res), 'idx', index, 'val', node.val)
            if len(res) == index:
                res.append(node.val)
            
            if node.right:
                queue.append((index+1, node.right))

            if node.left:
                queue.append((index+1, node.left))

        return res


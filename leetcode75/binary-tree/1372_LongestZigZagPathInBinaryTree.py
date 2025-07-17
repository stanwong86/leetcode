'''
This one took me some time because my count was off.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def traverse(root, max_count, current_count, last_zig):
            # print(max_count, current_count, last_zig)
            max_left = max_right = 0
            if root.left:
                if last_zig == 'right':
                    max_left = traverse(root.left, max_count, current_count+1, 'left')
                else:
                    max_left = traverse(root.left, max_count, 1, 'left')

            if root.right:
                if last_zig == 'left':
                    max_right = traverse(root.right, max_count, current_count+1, 'right')
                else:
                    max_right = traverse(root.right, max_count, 1, 'right')
            return max(max_count, current_count, max_left, max_right)
        
        return traverse(root, 0, 0, 'root')
                
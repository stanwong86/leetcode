'''
The left and right zig zag is tricky. Can use more practice
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        output = []
        left_to_right = True

        while queue:
            n = len(queue)    
            temp = []
            
            for i in range(n):
                if left_to_right:
                    node = queue.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    temp.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    
                    if node.left:
                        queue.appendleft(node.left)

            left_to_right = not left_to_right
            print(left_to_right)
            if temp:
                output.append(temp)

        return output
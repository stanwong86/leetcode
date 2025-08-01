"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            prev = None

            for i in range(n):
                node = queue.popleft()
                if not node:
                    continue

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

                if prev:
                    prev.next = node
                
                prev = node
        
        return root
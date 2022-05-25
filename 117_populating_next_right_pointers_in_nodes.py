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
        if not root:
            return root
        
        def traverse(node, level=0, d={}):
            if not node:
                return d
            
            if level not in d:
                d[level] = node
            else:
                d[level].next = node
                d[level] = node
            
            level += 1
            
            traverse(node.left, level, d)
            traverse(node.right, level, d)
        
        traverse(root)
        return root
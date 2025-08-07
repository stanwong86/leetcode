"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

This solution came after looking at a similar BFS approach.
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        queue = deque([node])
        clones = {node.val : Node(node.val, [])}
        
        while queue:
            cur = queue.popleft()
            
            for neighbor in cur.neighbors:
                if neighbor.val not in clones:
                    queue.append(neighbor)
                    clones[neighbor.val] = Node(neighbor.val, [])
                clones[cur.val].neighbors.append(clones[neighbor.val])
        return clones[node.val]


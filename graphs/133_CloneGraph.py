"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Took 50 minutes to solve the first time
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        def dfs(node, visited):
            if node.val in visited:
                return node.val, visited
            
            visited[node.val] = []
            
            for neighbor in node.neighbors:
                neighbor_val, visited = dfs(neighbor, visited)
                visited[node.val].append(neighbor_val)
            
            return node.val, visited

        _, visited = dfs(node, {})
        # print(visited)

        nodes_dict = {}
        def clone(val):
            if val in nodes_dict:
                return nodes_dict[val]
            
            nodes_dict[val] = Node(val, [])
            
            for visited_neighbor in visited[val]:
                # print(val, ': visited_neighbor:', visited_neighbor)
                neighbor_node = clone(visited_neighbor)
                nodes_dict[val].neighbors.append(neighbor_node)
            return nodes_dict[val]

        clone(1)
        # _, visited2 = dfs(nodes_dict[1], {})
        # print(visited2)
        return nodes_dict[1]
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()
        visited = set()
        all_connections = {}
        for a, b in connections:
            edges.add((a,b))
            if a not in all_connections:
                all_connections[a] = []
            all_connections[a].append(b)

            if b not in all_connections:
                all_connections[b] = []
            all_connections[b].append(a)
        

        queue = deque()
        queue.append(0)
        visited.add(0)
        edges_changed = 0
        
        while queue:
            city = queue.popleft()

            for neighbor in all_connections[city]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

                    if (neighbor, city) not in edges:
                        edges_changed += 1
        
        return edges_changed

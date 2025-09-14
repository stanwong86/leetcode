class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        minEdges = 0
        visited = set()
        edges = set()

        allConnections = {city: [] for city in range(n)}

        for i, node in enumerate(connections):
            a, b = node
            allConnections[a].append(b)
            allConnections[b].append(a)
            edges.add(tuple(node))
        
        queue = deque()
        queue.append(0)

        while queue:
            city = queue.popleft()
            # print('city', city)
            if city in visited:
                continue
            visited.add(city)
            neighbors = allConnections[city]

            for neighbor in neighbors:
               
                if neighbor not in visited:
                    queue.append(neighbor)
                
                    if (neighbor, city) not in edges:
                        # print('city, neighbor: ', city, neighbor)
                        minEdges += 1
        
        return minEdges
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        edges = set() # set is efficient for membership testing
        neighbors = {city: [] for city in range(n)}

        for a, b in connections:
            edges.add((a,b))
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city, count):
            if city not in visited:
                visited.add(city)

                for neighbor in neighbors[city]:
                    if neighbor not in visited and (neighbor, city) not in edges:
                        count += 1
                    count = dfs(neighbor, count)
            return count

        return dfs(0, 0)
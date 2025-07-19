import unittest

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        visited = edges = set()
        neighbors = {city: [] for city in range(n)}

        for a, b in connections:
            edges.add((a, b))
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city, count):
            visited.add(city)
            # print(f'city: {city} neighbors: {neighbors[city]}')
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                
                if (neighbor, city) not in edges:
                    count += 1

                count = dfs(neighbor, count)
            return count

        return dfs(0, 0)

class MyTests(unittest.TestCase):
    s = Solution()
    mainFunction = s.minReorder

    def test1(self):
        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

        actual = self.mainFunction(n, connections)
        expected = 3
        self.assertEqual(actual, expected)

    def test2(self):
        n = 5
        connections = [[1,0],[1,2],[3,2],[3,4]]

        actual = self.mainFunction(n, connections)
        expected = 2
        self.assertEqual(actual, expected)
    
    def test3(self):
        n = 3
        connections = [[1,0],[2,0]]

        actual = self.mainFunction(n, connections)
        expected = 0
        self.assertEqual(actual, expected)

unittest.main()
'''
The key is recognizing that there is either 1 node center or 2 node centers. If 3, that means 2 are leaves and should be stripped down to 1 node.
That's why we loop through until there are 2 nodes remaining
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        routes = defaultdict(list)
        degrees = [0] * n
        
        for a, b in edges:
            routes[a].append(b)
            routes[b].append(a)
            degrees[a] += 1
            degrees[b] += 1

        queue = deque()
        for i in range(n):
            if degrees[i] == 1:
                queue.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            size = len(queue)
            remaining_nodes -= size

            for _ in range(size):
                leaf = queue.popleft()

                for neighbor in routes[leaf]:
                    degrees[neighbor] -= 1

                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        return list(queue)
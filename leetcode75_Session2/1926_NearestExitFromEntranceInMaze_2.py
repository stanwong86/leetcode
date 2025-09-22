class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        m = len(maze)
        n = len(maze[0])

        minSteps = float('inf')

        queue = deque()
        queue.append((*entrance, 0))

        while queue:
            x, y, steps = queue.popleft()

            if (x == 0 or y == 0 or x == m-1 or y == n-1) and tuple(entrance) != (x,y):
                minSteps = min(minSteps, steps)
                return minSteps        
            
            for direction in directions:
                x1, y1 =  x + direction[0], y + direction[1]

                if 0 <= x1 < m and 0 <= y1 < n and maze[x1][y1] == '.' and (x1, y1) not in visited:
                    visited.add((x1,y1))
                    queue.append((x1, y1, steps + 1))

        return -1
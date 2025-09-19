class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        queue = deque()
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        m = len(grid)
        n = len(grid[0])

        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 1:
                    fresh.add((r, c))
                elif orange == 2:
                    queue.append((r, c))
        
        minutes = -1
        if not queue and not fresh:
            return 0
        while queue:
            size = len(queue)
            minutes += 1
            for _ in range(size):
                r, c = queue.popleft()
                
                for direction in directions:
                    x = r + direction[0]
                    y = c + direction[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x,y) in fresh:
                        queue.append((x, y))
                        fresh.remove((x,y))
        
        if not fresh:
            return minutes
        return -1
                    
        

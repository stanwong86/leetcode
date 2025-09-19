class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))
        
        minutes = 0
        while queue:
            r, c, minute = queue.popleft()
            minutes = max(minutes, minute)    
                
            for direction in directions:
                x = r + direction[0]
                y = c + direction[1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    queue.append((x, y, minutes+1))
                    grid[x][y] = 2
                    fresh -= 1
        
        if not fresh:
            return minutes
        return -1
                    
        

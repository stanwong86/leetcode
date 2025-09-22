class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        freshCount = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    freshCount += 1
        
        maxMinutes = 0
        while queue:
            x, y, minutes = queue.popleft()
            maxMinutes = max(maxMinutes, minutes)

            for direction in  directions:
                x1, y1 = x + direction[0], y + direction[1]

                if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1:
                    grid[x1][y1] = 2
                    freshCount -= 1
                    queue.append((x1, y1, minutes + 1))
        
        if freshCount > 0:
            return -1
        return maxMinutes
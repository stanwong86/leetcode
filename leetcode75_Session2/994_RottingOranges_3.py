class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        count = 0

        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        
        minute = -1
        while queue:
            minute += 1

            for _ in range(len(queue)):
                popped = queue.popleft()

                for direction in directions:
                    x = popped[0] + direction[0]
                    y = popped[1] + direction[1]

                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -= 1
                        queue.append((x, y))

        if count > 0:
            return -1
        return max(minute, 0)
                
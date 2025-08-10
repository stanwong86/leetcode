class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Initialize grid with all 1s
        grid = [[1] * n for r in range(m)]
        
        # First row and First col are already set as there is only 1 way.
        for i in range(1, m):
            for j in range(1, n):
                # Add previous cells above and to the left to get the total ways to get here.
                grid[i][j] = grid[i][j-1] + grid[i-1][j]

        # Return the bottom right cell
        return grid[-1][-1]

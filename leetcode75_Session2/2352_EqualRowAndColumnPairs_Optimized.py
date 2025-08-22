class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        row_counts = defaultdict(int)
        res = 0
        for row in grid:
            row_counts[tuple(row)] += 1
        
        # Basic Solution
        # for col in range(n):
        #     cols = []
        #     for row in range(n):
        #         cols.append(grid[row][col])
        #     res += row_counts[tuple(cols)]

        # Transposes grid
        for col in zip(*grid):
            res += row_counts[tuple(col)]
        
        return res
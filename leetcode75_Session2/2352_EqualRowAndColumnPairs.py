class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = defaultdict(int)
        cols = []
        
        # Cols
        for _ in range(n):
            cols.append([])
        
        count = 0
        for r in range(n):
            c = 0
            tup = tuple(grid[r])
            d[tup] += 1
            
            for val in grid[r]:
                cols[c].append(val)
                c += 1

        for row in d:
            for col in cols:
                # print(row, col)
                if row == tuple(col):
                    # print(row, col)
                    count += d[row]
        
        return count
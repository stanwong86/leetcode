class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for col in zip(*grid):
            for row in (grid):
                if tuple(row) == col:
                    count += 1
        return count
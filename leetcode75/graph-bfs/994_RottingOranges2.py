'''
2nd attempt: 5 minutes. Coding only
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        non_rotten = set()
        directions = [(0,1),(0,-1), (1,0), (-1,0)]
        min_minutes = 0

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    non_rotten.add((i,j))
                elif grid[i][j] == 2:
                    rotten.append([i, j, 0])

        while rotten and non_rotten:
            x, y, minutes = rotten.popleft()

            for direction in directions:
                x1, y1 = x+direction[0],y+direction[1]

                if 0 <= x1 < rows and 0 <= y1 < cols and (x1, y1) in non_rotten:
                    non_rotten.remove((x1,y1))
                    rotten.append([x1,y1,minutes+1])
                    min_minutes = max(min_minutes, minutes+1)
        
        if non_rotten:
            return -1
        return min_minutes
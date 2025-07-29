'''
1st attempt: 41 minutes.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Load all oranges into a queue. If orange is rotten, destroy surrounding oranges.
        # Rotten queue, add to rotten surrounding, add to visited
        # non-rotten queue

        rotten_queue = deque()
        non_rotten = set()
        min_minutes = 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_queue.append([(i, j), 0])
                elif grid[i][j] == 1:
                    non_rotten.add((i,j))
        
        # print('before- non_rotten:', non_rotten, ',rotten:', rotten_queue)
                
        while rotten_queue and non_rotten:
            move, minutes = rotten_queue.popleft()
            x, y = move

            # print('move:', move, ',non_rotten:', non_rotten, ',rotten:', rotten_queue)

            for direction in directions:
                x1, y1 = x+direction[0],y+direction[1]

                if 0 <= x1 < rows and 0 <= y1 < cols and (x1, y1) in non_rotten:
                    min_minutes = max(min_minutes, minutes+1)
                    rotten_queue.append([(x1,y1), minutes+1])
                    non_rotten.remove((x1,y1))
        
        if non_rotten:
            return -1
        return min_minutes
'''
Took me 67 minutes. A crucial hint was looking for the edge circles first and then we can mark the ones that are connected to the edge as non-surrounded ones.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        queue = deque() # Used for going through all circles
        circles = set() # Note all the circles that are not connected
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    circles.add((i,j))
                    queue.append((i,j))

        def findConnectedCircles(x, y):
            if (x,y) not in circles:
                return
            circles.remove((x,y))

            for direction in directions:
                x1, y1 = x+direction[0], y+direction[1]
                # print(f'({x1}, {y1}), {circles}')
                if 0 <= x1 < rows and 0 <= y1 < cols and (x1, y1) in circles:
                    # print(f'connected circles: ({x1}, {y1})')
                    findConnectedCircles(x1, y1)

        while queue:
            x, y = queue.popleft()

            if x == 0 or x == rows-1 or y == 0 or y == cols-1 and (x, y) in circles:
                # print(f'edges: ({x}, {y})')
                findConnectedCircles(x, y)
        
        for x, y in circles:
            board[x][y] = 'X'
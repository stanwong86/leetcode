class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        queue = deque()
        queue.append([*entrance, 0])
        minSteps = float('inf')

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while queue:
            x, y, steps = queue.popleft()
            # print(x, y, steps)
            if (x, y) in visited:
                continue
            
            # print('chk', y, len(maze[0]))
            if (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1) and (x, y) != tuple(entrance):
                minSteps = min(minSteps, steps)
                continue

            visited.add((x,y))

            for direction in directions:
                x1 = x + direction[0]
                y1 = y + direction[1]

                # print('x1, y1:', x1, y1)
                if 0 <= x1 < len(maze) and 0 <= y1 < len(maze[0]) and maze[x1][y1] == '.':
                    queue.append([x1, y1, steps+1])
        
        if minSteps == float('inf'):
            return -1
        return minSteps
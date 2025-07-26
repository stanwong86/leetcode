'''
This solution is copied and uses BFS
'''

import unittest
from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        visited = set()


        queue.append([tuple(entrance), 0]) # move, steps
        visited.add(tuple(entrance))

        directions = [(-1,0), (0, 1), (1, 0), (0, -1)] # left, up , right, down

        while queue:
            move, steps = queue.popleft()
            x, y = move

            if move != tuple(entrance) and (x == 0 or x == rows-1 or y == 0 or y == cols-1):
                return steps

            for x1, y1 in directions:
                x2, y2 = (x+x1, y+y1)
                if 0 <= x2 < rows and 0 <= y2 < cols and (x2,y2) not in visited and maze[x2][y2] != '+':
                    queue.append([(x2,y2), steps+1])
                    visited.add((x2,y2))
        
        return -1


class MyTests(unittest.TestCase):
    s = Solution()
    f = s.nearestExit

    def test1(self):
        maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
        entrance = [1,2]
        self.assertEqual(self.f(maze, entrance), 1)

    def test2(self):
        maze = [["+","+","+"],[".",".","."],["+","+","+"]]
        entrance = [1,0]
        self.assertEqual(self.f(maze, entrance), 2)

    def test3(self):
        maze = [[".","+"]]
        entrance = [0,0]
        self.assertEqual(self.f(maze, entrance), -1)
    
    def test4(self):
        maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
        entrance = [0,1]
        self.assertEqual(self.f(maze, entrance), 12)

    def test5(self):
        maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]
        entrance = [0,1]
        self.assertEqual(self.f(maze, entrance), 7)
    
    def test6(self):
        maze = [["."]]
        entrance = [0,0]
        self.assertEqual(self.f(maze, entrance), -1)

unittest.main()
    

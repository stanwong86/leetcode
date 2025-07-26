'''
BFS Practice
1st. 8 minutes
2nd. 4m 36s
3rd. 3m
'''

import unittest
from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        visited = set()

        queue.append([tuple(entrance), 0])
        visited.add(tuple(entrance))

        directions = [(0,1), (0, -1), (1,0), (-1,0)]

        while queue:
            move, steps = queue.popleft()
            x, y = move

            if move != tuple(entrance) and (x == 0 or x == rows-1 or y == 0 or y == cols-1):
                return steps
            
            for direction in directions:
                x1, y1 = x+direction[0], y+direction[1]

                if 0 <= x1 < rows and 0 <= y1 < cols and maze[x1][y1] != '+' and (x1, y1) not in visited:
                    queue.append([(x1, y1), steps+1])
                    visited.add((x1,y1))

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
    

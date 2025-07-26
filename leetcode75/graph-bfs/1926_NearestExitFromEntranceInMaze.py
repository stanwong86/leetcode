'''
First Attempt at this using DFS. It is too slow and gets timed out.
'''

import unittest

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        memo = {}
        min_exit = float('inf')
        
        def dp(move, steps):
            nonlocal min_exit
            print('move: ', move, ',steps:', steps)
            x, y = move

            if move in memo and memo[move] <= steps:
                print('exists')
                return memo[move]

            if x < 0 or x == len(maze) or y < 0 or y == len(maze[0]):
                print('Out of Bounds')
                return float('inf')

            if maze[x][y] == '+':
                print('Wall')
                memo[(x,y)] = float('inf')
                return float('inf')
            
            memo[(x,y)] = steps

            if (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1) and steps > 0:
                print('Found Exit')
                min_exit = min(min_exit, steps)
                print(min_exit, steps)
                # print('move, entrance:', move, entrance)
                return steps
            
            steps += 1
            left = dp((x-1, y), steps)
            up = dp((x, y+1), steps)
            right = dp((x+1, y), steps)
            down = dp((x, y-1), steps)
        
        dp(tuple(entrance), 0)
        # print('min_exit:', min_exit)
        return -1 if min_exit == float('inf') else min_exit


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

unittest.main()
    

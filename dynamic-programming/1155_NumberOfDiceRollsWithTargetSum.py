'''
You have n dice, and each dice has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
'''
import unittest

class Solution:
    def numRollsToTarget(self, dice: int, face: int, target: int) -> int:
        dp = {}  
        def roll(dice, target):
            if dice == 0:
                return 0 if target > 0 else 1
            if (dice, target) in dp:
                return dp[(dice, target)]
            
            to_return = 0
            for face_value in range(1, min(face, target)+1):
                to_return += roll(dice - 1, target - face_value)
            
            dp[(dice, target)] = to_return
            return to_return

        return roll(dice, target) % (10**9 + 7)

class MyTests(unittest.TestCase):
    s = Solution()
    mainFunction = s.numRollsToTarget

    def test1(self):
        actual = self.mainFunction(1, 6, 3)
        self.assertEqual(actual, 1)

    # def test2(self):
    #     actual = self.mainFunction(2, 6, 7)
    #     self.assertEqual(actual, 6)

    # def test3(self):
    #     actual = self.mainFunction(30, 30, 500)
    #     self.assertEqual(actual, 222616187)

unittest.main()
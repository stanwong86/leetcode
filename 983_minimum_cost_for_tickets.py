'''
Return the minimum number of dollars you need to travel every day in the given list of days.
------------------
This solution uses Dynamic Programming to calculate the cost of all 365 calendar days. For each day, we calculate the cost of buying each pass.
We take the minimum of buying the passes with respect to x days before. We save the min to today's cost. At the end, we take the last day to be
the cheapest day.
'''


import unittest

class Solution(unittest.TestCase):
    def mincostTickets(self, days: list[int], costs: list):
        dp = [0] * 366

        for i in range(1, 366):
            if i in days:
                # Days of Travel
                pass1 = dp[i-1] + costs[0]
                pass7 = dp[max(0, i-7)] + costs[1]
                pass30 = dp[max(0, i-30)] + costs[2]
                dp[i] = min(pass1, pass7, pass30)
            else:
                dp[i] = dp[i-1]
        return max(dp)

    def test_example1(self):
        days = [1,4,6,7,8,20]
        costs = [2,7,15]
        expected = 11
        
        actual = self.mincostTickets(days, costs)
        self.assertEqual(actual, expected)

    def test_example2(self):
        days = [1,2,3,4,5,6,7,8,9,10,30,31]
        costs = [2,7,15]
        expected = 17
        
        actual = self.mincostTickets(days, costs)
        self.assertEqual(actual, expected)

    def test_example3(self):
        days = [1,4,8,9,11]
        costs = [2,7,15]
        expected = 10
        
        actual = self.mincostTickets(days, costs)
        self.assertEqual(actual, expected)

unittest.main()
# unittest.main(Solution().test_example1())
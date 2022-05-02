import unittest

class Solution(unittest.TestCase):
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x

        while l <= r:
            mid = l + (r-l) // 2
            value = mid*mid

            if value < x:
                l = mid+1
            else:
                r = mid-1
        # print(l, r)
        return l

    def tests(self):
        self.assertEqual(self.mySqrt(1), 1)
        self.assertEqual(self.mySqrt(16), 4)
        self.assertEqual(self.mySqrt(0), 0)

unittest.main()
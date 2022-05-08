import unittest

class Solution(unittest.TestCase):
    def merge(self, nums: list, m: int, nums2: list, n: int) -> list:
        a = 0
        b = 0

        while b < n:
            if a >= (m + b) or nums[a] >= nums2[b]:
                nums.insert(a, nums2[b])
                b += 1
                a += 1
                nums.pop(-1)
            else:
                a += 1
        return nums


    def tests(self):
        n = [1,2,3,0,0,0]
        self.merge(n, 3, [2,5,6], 3)
        self.assertEqual(n, [1,2,2,3,5,6])

        r = self.merge([1], 1, [], 0)
        self.assertEqual(r, [1])

        r = self.merge([0], 0, [1], 1)
        self.assertEqual(r, [1])

unittest.main()
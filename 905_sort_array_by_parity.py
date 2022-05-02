import unittest

class Solution(unittest.TestCase):
    def sortArrayByParity(self, nums: list) -> list:
        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] % 2 == 1:
                if nums[r] % 2 == 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        return nums

    def tests(self):
        r = self.sortArrayByParity([3,1,2,4])
        # print(r)
        self.assertTrue(r in [[4,2,3,1], [2,4,1,3], [4,2,1,3]])
        self.assertEqual(self.sortArrayByParity([0]), [0])
        self.assertEqual(self.sortArrayByParity([1]), [1])

unittest.main()
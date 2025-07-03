'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2 zeroes = all 0s
        # 1 zero = 0s except self
        # 0 zero = use Product / self

        n = len(nums)
        zeroCount = 0
        product = 1
        lastZeroIndex = -1
        for i in range(n):
            if nums[i] == 0:
                zeroCount += 1
                lastZeroIndex = i
            else:
                product *= nums[i]
        
        allZeroes = [0] * n
        if zeroCount >= 2:
            return allZeroes
        elif zeroCount == 1:
            allZeroes[lastZeroIndex] = product
            return allZeroes
        else:
            newNums = [int(product/num) for num in nums]
            return newNums

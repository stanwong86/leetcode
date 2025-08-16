class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        zeroPos = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                zeroPos = i
            else:
                product *= nums[i]
        
        zeroArray = [0] * len(nums)

        if zeroCount >= 2:
            return zeroArray
        elif zeroCount == 1:
            zeroArray[zeroPos] = product
            return zeroArray
        else:
            return [product // num for num in nums]

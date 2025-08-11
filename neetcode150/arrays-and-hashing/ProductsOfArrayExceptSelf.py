class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        product = 1
        zeroCountPos = -1

        m = len(nums)
        for i in range(m):
            if nums[i] == 0:
                zeroCount += 1
                zeroCountPos = i
            else:
                product *= nums[i]
        
        allZeroes = [0] * m 
        if zeroCount >= 2:
            return allZeroes
        elif zeroCount == 1:
            allZeroes[zeroCountPos] = product
            return allZeroes
        else:
            return [product//n for n in nums]
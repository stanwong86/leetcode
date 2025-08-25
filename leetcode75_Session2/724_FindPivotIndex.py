class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftTotal = 0
        rightTotal = sum(nums)

        i = 0

        while i < len(nums):
            if leftTotal == rightTotal - nums[i]:
                return i
            
            leftTotal += nums[i]
            rightTotal -= nums[i]
            i += 1
        return -1
        
            
            
            
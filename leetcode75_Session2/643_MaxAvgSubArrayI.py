class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        runningSum = 0
        maxAvg = -float('inf')
        for i in range(len(nums)-k+1):
            if i == 0:
                print(nums, i, i+k)
                runningSum = sum(nums[i:i+k])
            else:
                runningSum = runningSum - nums[i-1] + nums[i+k-1]
            maxAvg = max(maxAvg, runningSum / k)
        return maxAvg
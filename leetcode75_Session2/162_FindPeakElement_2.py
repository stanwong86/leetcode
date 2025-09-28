class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if 0 <= mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        
        return l
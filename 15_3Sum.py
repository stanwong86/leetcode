class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        trips = []

        nums.sort()
        if max(nums) < 0 or min(nums) > 0:
            return trips

        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            X = -nums[i]
            j = i+1
            k = len(nums)-1

            while j < k:
                if (nums[j] + nums[k]) == X:
                    trips.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j-1] == nums[j]:
                        j += 1

                    while j < k and nums[k+1] == nums[k]:
                        k -= 1

                elif (nums[j] + nums[k]) < X:
                    j += 1
                else:
                    k -= 1
        return trips

s = Solution()
nums = [-1,0,1,2,-1,-4]
nums = []
nums = [0]
nums = [0,0,0]
nums = [-1,0,0]
nums = [1,2,-2,-1]
r = s.threeSum(nums)
print(r)
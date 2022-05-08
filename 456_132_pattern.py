class Solution:
    def find132pattern(self, nums) -> bool:
        if len(nums) < 3:
            return False
    
        stack = []
        second_num = float('-inf')
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < second_num:
                return True
            
            print(stack)
            while stack and stack[-1] < nums[i]:
                print('pop', stack)
                second_num = stack.pop()
            
            stack.append(nums[i])
        
        return False

s = Solution()
# nums = [1,2,3,4]
# nums = [3,1,4,2] # True
# nums = [1,0,1,-4,-2] # False
# nums = [1,0,1,-4,-2,-3] # True
# nums = [0,-1000,2000,-3000,4000,-5000,6000,-7000,8000,-9000,10000]
# nums = [0,10,0,5,0,5,0]
nums = [2,4,-1,3]
r = s.find132pattern(nums)
print(r)
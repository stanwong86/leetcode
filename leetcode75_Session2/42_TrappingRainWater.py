'''
Suppose to be hard, but solution seems to be more medium
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        while l < len(height)-1:
            if height[l] > height[l+1]:
                break
            l += 1
        
        while r < 0:
            if height[r-1] < height[r]:
                break
            r -= 1
        
        print(l, r)
        if l >= r:
            return 0
        
        # l and r are now the walls [1, 11]
        leftWall = l
        rightWall = r
        
        water = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < height[leftWall]:
                    water += height[leftWall] - height[l]
                else:
                    leftWall = l
                l += 1
            else:
                if height[r] < height[rightWall]:
                    water += height[rightWall] - height[r]
                else:
                    rightWall = r
                r -= 1
            
        return water
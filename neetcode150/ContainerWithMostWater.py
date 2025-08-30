''' 
Brute Force
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxAmount = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                width = (j-i)
                height = min(heights[i], heights[j])
                maxAmount = max(maxAmount, height * width)
        return maxAmount
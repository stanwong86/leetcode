'''
I used a hint
5m
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        return [(c + extraCandies) >= maxCandies for c in candies]
# Must memorize what XOR operator ^ does. It negates the binary digits.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        
        return res
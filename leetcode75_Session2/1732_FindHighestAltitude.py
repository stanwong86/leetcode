class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        high = 0

        for g in gain:
            res += g

            high = max(high, res)
        return high
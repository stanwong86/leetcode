class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 1
        high = piles[-1]
        ans = high

        while low <= high:
            mid = (low + high) // 2

            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort() # n log(n)

        if len(piles) < 2:
            return ceil(piles[0] / h)
        
        l = 1
        r = piles[-1]
        minK = r

        while l <= r:
            k = (l + r) // 2
            hours = sum(ceil(n/k) for n in piles)
            print(l, r, k, hours)

            if hours <= h:
                minK = k
                r = k-1
            else:
                l = k+1
        
        return minK
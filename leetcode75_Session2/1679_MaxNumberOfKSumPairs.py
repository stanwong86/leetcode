class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        
        # Same numbers
        # target -num = dict num

        opsCount = 0
        for n in nums:
            if d[k-n]:
                d[k-n] -= 1
                opsCount += 1
            else:
                d[n] += 1
        
        return opsCount
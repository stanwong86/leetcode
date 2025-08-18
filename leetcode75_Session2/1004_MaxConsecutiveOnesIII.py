class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        onesCount = 0
        zeroCount = 0
        window = []
        maxNum = 0

        for n in nums:
            if n == 1:
                onesCount += 1
            else:
                zeroCount += 1
            
            window.append(n)

            while zeroCount > k:
                popped = window.pop(0)
                if popped == 1:
                    onesCount -= 1
                else:
                    zeroCount -= 1
            
            maxNum = max(maxNum, len(window))
        return maxNum
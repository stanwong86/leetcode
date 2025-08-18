leetcode75_Session2/1493_LongestSubarrayOf1sAfterDeletingOneElement.pyclass Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroesCount = 0
        onesCount = 0
        window = []
        longest = 0

        for n in nums:
            if n == 1:
                onesCount += 1
            else:
                zeroesCount += 1
            
            window.append(n)

            while zeroesCount > 1:
                popped = window.pop(0)
                if popped == 1:
                    onesCount -= 1
                else:
                    zeroesCount -= 1
            
            longest = max(longest, len(window)-1)
        return longest
                
'''
Meta question
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totals = {0: 1}

        total = count = 0

        for num in nums:
            total += num

            if total-k in totals:
                count += totals[total-k]
            
            if total not in totals:
                totals[total] = 0
            totals[total] += 1
        
        return count

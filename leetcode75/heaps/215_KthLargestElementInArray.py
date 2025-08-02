class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        largest = heapq.nlargest(k, nums)
        print(largest)
        return largest[-1]
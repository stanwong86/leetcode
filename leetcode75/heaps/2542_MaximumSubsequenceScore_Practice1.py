class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_list = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        heap = []
        total = max_score = 0
        for n1, n2 in sorted_list:
            heapq.heappush(heap, n1)
            total += n1

            if len(heap) > k:
                total -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, total * n2)
        return max_score
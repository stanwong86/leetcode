class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = [(freq, val) for val, freq in counts.items()]
        heapq.heapify(heap)

        largest = heapq.nlargest(k, heap)
        vals = [val for freq, val in largest]
        return vals
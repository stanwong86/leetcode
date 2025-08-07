class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        heap = [(val, key) for key,val in counts.items()]
        heapq.heapify(heap)
        largest = heapq.nlargest(k, heap)
        print(largest)
        return [v for f,v in largest]
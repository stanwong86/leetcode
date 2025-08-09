class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = 0
        r = len(costs) - 1

        pq1 = []
        pq2 = []

        ans = 0

        while k > 0:
            while len(pq1) < candidates and l <= r:
                heapq.heappush(pq1, costs[l])
                l += 1
            
            while len(pq2) < candidates and l <= r:
                heapq.heappush(pq2, costs[r])
                r -= 1

            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')

            if t1 <= t2:
                ans += t1
                heapq.heappop(pq1)
            else:
                ans += t2
                heapq.heappop(pq2)
            k -= 1
        return ans
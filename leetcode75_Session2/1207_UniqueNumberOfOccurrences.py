class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for n in arr:
            d[n] += 1
        
        return len(set(d.values())) == len(d.values())
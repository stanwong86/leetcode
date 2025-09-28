class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        visited_spells = defaultdict(int)
        res = []

        for spell in spells:
            if spell in visited_spells:
                res.append(visited_spells[spell])
                continue
            l = 0
            r = len(potions)-1
            while l <= r:
                mid = (l+r) // 2

                if spell * potions[mid] < success:
                    l = mid+1
                else:
                    r = mid-1
                
            pairsCount = len(potions) - l
            res.append(pairsCount)
            visited_spells[spell] = pairsCount
        return res
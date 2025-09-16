class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        d = {}
        potions.sort()
        arr = []

        for spell in spells:
            if spell in d:
                arr.append(d[spell])
                continue

            l = 0
            r = len(potions)-1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid]*spell < success:
                    l = mid + 1
                else:
                    r = mid - 1
            count = len(potions) - l
            arr.append(count)
            
            d[spell] = count
        return arr
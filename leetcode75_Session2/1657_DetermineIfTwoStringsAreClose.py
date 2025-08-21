class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in word1:
            d1[c] += 1
        
        for c in word2:
            d2[c] += 1
        
        if set(d1.keys()) != set(d2.keys()):
            return False

        l1 = list(d1.values())
        l2 = list(d2.values())
        l1.sort()
        l2.sort()
        print(l1)
        print(l2)
        
        return l1 == l2
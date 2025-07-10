from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            d[sorted_word].append(word)
        
        final = []
        for values in d.values():
            final.append(values)

        return final
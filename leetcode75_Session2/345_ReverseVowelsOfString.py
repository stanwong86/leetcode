class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list('aeiouAEIOU')
        listS = list(s)
        
        l = 0
        r = len(listS) - 1

        while l <= r:
            while l <= r and listS[l] not in vowels:
                l += 1
            while l <= r and listS[r] not in vowels:
                r -= 1
            
            if l <= r:
                listS[l], listS[r] = listS[r], listS[l]
                l += 1
                r -= 1
        
        return ''.join(listS)
            

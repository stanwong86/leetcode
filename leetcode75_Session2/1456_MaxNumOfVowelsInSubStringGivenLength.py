class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = 'aeiou'
        listS = list(s)
        window = listS[:k]
        vowelCount = sum(1 if c in vowels else 0 for c in window)
        maxVowelCount = vowelCount

        for i in range(1, len(s)-k+1):
            if window[0] in vowels:
                vowelCount -= 1
                
            newChar = listS[i+k-1]
            if newChar in vowels:
                vowelCount += 1

            window.pop(0)
            window.append(newChar)
            maxVowelCount = max(maxVowelCount, vowelCount)
        
        return maxVowelCount


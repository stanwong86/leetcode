'''

22 minutes. Failed 2 submissions
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        m = len(str1)
        n = len(str2)
        
        for letterCount in range(n, 0, -1):
            if m % letterCount != 0 and n % letterCount != 0:
                continue
            
            quotient1 = m // letterCount
            quotient2 = n // letterCount

            for i in range(0, n-quotient2+1):
                substring = str2[i:i+letterCount]
                if str1 == substring * quotient1 and str2 == substring * quotient2:
                    return substring
        
        return ""
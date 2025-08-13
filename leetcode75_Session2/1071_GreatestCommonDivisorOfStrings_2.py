'''
7m12s
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ""
        def isDivisible(word, divisor):
            if len(word) % len(divisor) != 0:
                return False
            
            quotient = len(word) // len(divisor)

            return word == (divisor * quotient)
        
        i = 1
        while i <= len(str1) and i <= len(str2):
            divisor = str1[:i]
            if isDivisible(str1, divisor) and isDivisible(str2, divisor):
                gcd = divisor
            i += 1
        return gcd
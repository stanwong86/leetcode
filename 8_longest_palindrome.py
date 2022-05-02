class Solution:
    def longestPalindrome(self, s: str) -> str:
        outputString = ''
        for i in range(len(s)):
            odd = self.palindrome(s, i, i)
            even = self.palindrome(s, i, i+1)

            outputString = max(odd, even, outputString, key=len)
        return outputString
    
    def palindrome(self, s, l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        
        return s[l+1: r]

s = "babbad"
# res = longestPalindrome(s)
# print(res)

sol = Solution()
# res = sol.palindrome(s, 2, 3)
res = sol.longestPalindrome(s)
print(res)
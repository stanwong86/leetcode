# 2 min
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        return ' '.join(s[::-1])
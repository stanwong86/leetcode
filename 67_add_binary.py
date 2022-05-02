class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        x = bin(a + b)
        print(x[2:])


s = Solution()
s.addBinary("11", "1")
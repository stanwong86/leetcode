class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(list(bin(i)[2:]).count('1'))

        return result
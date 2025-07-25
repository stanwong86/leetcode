class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            
            if bit_c == 0:
                flips += (bit_a + bit_b)
            else:
                # a/b = 0/0 flips once
                if bit_a == bit_b == 0:
                    flips += 1
                # a/b = 1/1, 0/1, 1/0 flips zero
            a >>= 1
            b >>= 1
            c >>= 1
        
        return flips
                
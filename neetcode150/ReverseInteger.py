class Solution:
    def reverse(self, x: int) -> int:
       
        sign = ''
        if x < 0:
            sign = '-'
            x *= -1
        
        s = str(x)
        s = sign + s[::-1]
        
        i = int(s)
        
        if i < -(2**31) or i > 2**31-1:
            return 0
        return i
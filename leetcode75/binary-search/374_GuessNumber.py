# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        g = None
        l, r = 1, n
        while l <= r:
            pick = (l+r) // 2
            g = guess(pick)
            # print(f'l:{l}, r:{r}, pick:{pick}, g:{g}')
            if g < 0:
                r = pick-1
            elif g > 0:
                l = pick+1
            else:
                return pick
        return pick
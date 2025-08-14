class Solution:
    def isPalindrome(self, s: str) -> bool:
        listS = list(filter(lambda x: x.isalnum(), list(s)))
        print(listS)
        l = 0
        r = len(listS) - 1

        while l <= r:
            if listS[l].lower() != listS[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
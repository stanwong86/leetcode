class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        listS = list(s)
        for c in t:
            if len(listS) == 0:
                return True

            if c == listS[0]:
                listS.pop(0)
        
        return len(listS) == 0

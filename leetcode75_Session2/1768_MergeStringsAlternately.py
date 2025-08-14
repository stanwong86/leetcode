class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        list1 = list(word1)
        list2 = list(word2)
        ans = []
        while list1 or list2:
            if not list1:
                ans.extend(list2)
                break
            if not list2:
                ans.extend(list1)
                break
            
            c1 = list1.pop(0)
            c2 = list2.pop(0)
            ans.append(c1)
            ans.append(c2)
        
        return ''.join(ans)

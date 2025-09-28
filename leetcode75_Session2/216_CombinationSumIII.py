class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        def backtrack(combinations, currentSum):
            lenC = len(combinations)
            if lenC == k:
                if currentSum == n:
                    res.append(combinations)
                return
                    
            if combinations:
                nextNum = combinations[-1] + 1
            else:
                nextNum = 1
            
            for i in range(nextNum, min(9, n)+1):
                if currentSum + i > n and len(combinations)+1 <= k:
                    break
                backtrack(combinations + [i], currentSum + i)
                
        backtrack([], 0)
        return res
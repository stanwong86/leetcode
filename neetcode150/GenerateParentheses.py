# Use backtracking - safe to pass list by reference

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, openCount, closeCount):
            if openCount == n and closeCount == n:
                res.append(''.join(curr))
                return
                
            # Add opened
            if openCount < n:
                curr.append('(')
                backtrack(curr, openCount+1, closeCount)
                curr.pop()
            
            # Add closing
            if closeCount < openCount:
                curr.append(')')
                backtrack(curr, openCount, closeCount+1)
                curr.pop()
        
        backtrack([], 0, 0)

        # print(res)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> list:

        def backtrack(leftCount, rightCount, n, pattern, result):

            if len(pattern) == (n * 2):
                result.append(pattern)
                return result

            if leftCount < n:
                backtrack(leftCount+1, rightCount, n, pattern + '(', result)

            if rightCount < leftCount:
                backtrack(leftCount, rightCount+1, n, pattern + ')', result)
        result = []
        backtrack(0, 0, n, '', result)
        print(result)


s = Solution()
r = s.generateParenthesis(4)
print(r)

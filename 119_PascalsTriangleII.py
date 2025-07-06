'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]
'''

# This solution is faster and uses less memory than dynamic programming memoization
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = {}
        memo[0] = [1]
        memo[1] = [1, 1]

        for i in range(2, rowIndex+1):
            prevRow = memo[i-1]
            row = []
            for j in range(len(prevRow)-1):
                row.append(prevRow[j] + prevRow[j+1])
            
            memo[i] = [1] + row + [1]
        
        return memo[rowIndex]
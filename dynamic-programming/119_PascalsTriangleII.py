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

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = {}
        memo[0] = [1]
        memo[1] = [1, 1]

        def pascal(rowIndex):
            if rowIndex in memo:
                return memo[rowIndex]
            else:
                prevRow = pascal(rowIndex-1)
            arr = []
            for i in range(len(prevRow)-1):
                arr.append(prevRow[i] + prevRow[i+1])
            return [1] + arr + [1]
        
        return pascal(rowIndex)
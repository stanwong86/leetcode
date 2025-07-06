'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
'''

# Need to learn itertools since it has useful tools like combinations.

import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        low = '123456789'
        high = '987654321'

        result = []

        start = int(low[:k])
        end = int(high[:k])+1

        combinations = list(itertools.combinations(list(low), k))

        for c in combinations:            
            numList = [int(j) for j in c]
            if sum(numList) == n:
                result.append(numList)

        return result
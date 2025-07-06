'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''

import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = 'abcdefghijklmnopqrstuvwxyz'
        d = {
            2: s[0:3],
            3: s[3:6],
            4: s[6:9],
            5: s[9:12],
            6: s[12:15],
            7: s[15:19],
            8: s[19:22],
            9: s[22:26]
        }

        permutations = []
        for i in range(len(digits)):
            letters_list = list(d[int(digits[i])])
            if i == 0:
                permutations = letters_list
            else:
                permutations = [x + y for (x, y) in itertools.product(permutations, letters_list)]
        # print(permutations)
        return permutations